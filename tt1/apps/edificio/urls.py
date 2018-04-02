from django.urls import path, include
from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from apps.edificio.views import listadousuarios,index,edificio_view,edificio_list,edificio_edit, \
	EdificioList, EdificioCreate, EdificioUpdate, EdificioDelete

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^nuevo$', login_required(EdificioCreate.as_view()), name='edificio_crear'),
    url(r'^listar', login_required(EdificioList.as_view()), name='edificio_listar'),
    url(r'^editar/(?P<pk>\d+)/$', login_required(EdificioUpdate.as_view()), name='edificio_editar'),
    url(r'^eliminar/(?P<pk>\d+)/$', login_required(EdificioDelete.as_view()), name='edificio_eliminar'),
    url(r'^listado', listadousuarios, name="listado"),
]