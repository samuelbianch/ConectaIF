from datetime import datetime

class Make_Graph():

	def __init__(self, lista_arestas, direcionada):
		today = datetime.now()
		ano = str(today.year)
		if today.month < 10:
			mes = "0" + str(today.month)
		else:
			mes = str(today.month)

		if today.day < 10:
			dia = "0" + str(today.day)
		else:
			dia = str(today.day)

		with open("/media/redes/"+ ano + mes + dia + "/" + lista_arestas.name) as arquivo:
			self.lista_arestas = arquivo.readlines()
			arquivo.close()
		self.direcionada = direcionada
		print("Lista de arestas: ")
		print(self.lista_arestas)

	def plot_graph(self):
		import igraph
		import time

		grafo = igraph.Graph()
		grafo = grafo.Read_Edgelist(self.lista_arestas, directed=self.direcionada)

		i = 0
		vertices = grafo.vcount()
		vindex1=[""]*vertices

		self.arestas = grafo.ecount()
		self.vertices = grafo.vcount()
		self.reciprocidade = grafo.reciprocity()
		self.assortatividade = grafo.assortativity_degree()
		self.mediatrans = grafo.transitivity_avglocal_undirected()

		igraph.plot(grafo, "/aplicacao/static/redes/" + time.time() + ".svg", bbox=(800, 700), margin=20, vertex_label=vindex1, edge_arrow_size=0.3, vertex_color=(255, 0, 0), vertex_label_color=(225, 225, 0), vertex_label_size=1, vertex_dist=200)

	def monta_contexto(self):
		contexto = {
			"arestas": self.arestas,
			"vertices": self.vertices,
			"reciprocidade": self.reciprocidade,
			"assortatividade": self.assortatividade,
			"mediatrans": self.mediatrans,
		}

		return contexto