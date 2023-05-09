from datetime import datetime
import igraph
import time

class Make_Graph():

	def __init__(self, lista_arestas, direcionada):
		today = datetime.now()
		ano = str(today.year)
		grafo = igraph.Graph()

		if today.month < 10:
			mes = "0" + str(today.month)
		else:
			mes = str(today.month)

		if today.day < 10:
			dia = "0" + str(today.day)
		else:
			dia = str(today.day)

		with open("media/redes/"+ ano + mes + dia + "/" + lista_arestas.name) as arquivo:
			grafo = grafo.Read_Edgelist(arquivo, directed=direcionada)
			arquivo.close()

		self.grafo = grafo

	def plot_graph(self):
		return igraph.plot(self.grafo, "aplicacao/static/redes/" + str(time.time()) + ".svg")

	def monta_contexto(self):
		arestas = self.grafo.ecount()
		vertices = self.grafo.vcount()
		reciprocidade = self.grafo.reciprocity()
		assortatividade = self.grafo.assortativity_degree()
		mediatrans = self.grafo.transitivity_avglocal_undirected()

		contexto = {
			"arestas": round(arestas,2),
			"vertices": round(vertices,2),
			"reciprocidade": round(reciprocidade,2),
			"assortatividade": round(assortatividade,2),
			"mediatrans": round(mediatrans,2),
			"imagem" : self.plot_graph()
		}

		return contexto