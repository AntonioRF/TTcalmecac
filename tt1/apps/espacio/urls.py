from django.urls import path
from django.conf.urls import url
from apps.espacio.views import EspacioList, EspacioCreate, EspacioUpdate, \
	EspacioDelete

urlpatterns = [
    #path('', index_adopcion),
    path('espacio/listar', EspacioList.as_view(), name='espacio_listar'),
    path('espacio/nueva', EspacioCreate.as_view(), name='espacio_crear'),
    #path('solicitud/editar/', SolicitudCreate.as_view(), name='solicitud_crear'),
    url(r'^espacio/editar/(?P<pk>\d+)/$', EspacioUpdate.as_view(), name='espacio_editar'),
    url(r'^espacio/eliminar/(?P<pk>\d+)/$', EspacioDelete.as_view(), name='espacio_eliminar'),
]