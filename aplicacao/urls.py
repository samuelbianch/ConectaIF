from django.urls import include, path
from . import views
from rest_framework import routers
from aplicacao.views import ArtigosViewSet, AutoresViewSet, RedesViewSet

router = routers.DefaultRouter()
router.register('redes', RedesViewSet, basename='Redes')
router.register('autores', AutoresViewSet, basename='Autores')
router.register('artigos', ArtigosViewSet, basename='Artigos')

urlpatterns = [
    path('', views.index, name='ConectaIF'),
    path('api/', include(router.urls)),
    path('artigos_publicados', views.artigos_publicados, name='artigos_publicados'),
    path('como_fazer', views.como_fazer, name='como_fazer')
]
