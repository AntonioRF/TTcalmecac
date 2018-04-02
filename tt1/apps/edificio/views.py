from django.shortcuts import render, redirect
from django.http import HttpResponse
from apps.edificio.forms import EdificioForm
from apps.edificio.models import Edificio
from django.urls import reverse,reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.core import serializers
from django.contrib.auth.models import User

# Create your views here.


def listadousuarios(request):
	lista = serializers.serialize('json', User.objects.all(), fields=['username','first_name'])
	return HttpResponse(lista, content_type='application/json')

def index(request):
	return render(request, 'edificio/index.html')

def edificio_view(request):
	if request.method == 'POST':
		form = EdificioForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect('index')
	else:
		form = EdificioForm()

	return render(request, 'edificio/edificio_form.html', {'form':form})

def edificio_list(request):
	edificio = Edificio.objects.all().order_by('id')
	contexto = {'edificio':edificio}
	return render(request, 'edificio/edificio_list.html',contexto)

def edificio_edit(request, id_edificio):
	edificio = Edificio.objects.get(id=id_edificio)
	if request.method == 'GET':
		form = EdificioForm(instance=edificio)
	else:
		form = EdificioForm(request.POST, instance=edificio)
		if form.is_valid():
			form.save()
		return redirect('edificio_listar')
	return render(request, 'edificio/edificio_form.html',{'form':form})

def mascota_delete(request, id_edificio):
	edificio = Edificio.objects.get(id=id_edificio)
	if request.method == 'POST':
		edificio.delete()
		return redirect('edificio_listar')
	return render(request, 'edificio/edificio_delete.html',{'edificio':edificio})


class EdificioList(ListView):
	model = Edificio
	template_name = 'edificio/edificio_list.html'

class EdificioCreate(CreateView):
	model = Edificio
	form_class = EdificioForm
	template_name = 'edificio/edificio_form.html'
	success_url = reverse_lazy('edificio_listar')

class EdificioUpdate(UpdateView):
	model = Edificio
	form_class = EdificioForm
	template_name = 'edificio/edificio_form.html'
	success_url = reverse_lazy('edificio_listar')

class EdificioDelete(DeleteView):
	model = Edificio
	form_class = EdificioForm
	template_name = 'edificio/edificio_delete.html'
	success_url = reverse_lazy('edificio_listar')