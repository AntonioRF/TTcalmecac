from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from apps.espacio.models import Espacio
from apps.espacio.forms import EspacioForm
from django.urls import reverse,reverse_lazy

# Create your views here.

class EspacioList(ListView):
	model = Espacio
	template_name = 'espacio/espacio_list.html'

class EspacioCreate(CreateView):
	model = Espacio
	form_class = EspacioForm
	template_name = 'espacio/espacio_form.html'
	success_url = reverse_lazy('espacio_listar')

class EspacioUpdate(UpdateView):
	model = Espacio
	form_class = EspacioForm
	template_name = 'espacio/espacio_form.html'
	success_url = reverse_lazy('espacio_listar')

class EspacioDelete(DeleteView):
	model = Espacio
	form_class = EspacioForm
	template_name = 'espacio/espacio_delete.html'
	success_url = reverse_lazy('espacio_listar')