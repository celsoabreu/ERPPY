# -*- coding: utf-8 -*-
from django.http import Http404
from django.shortcuts import render_to_response, render, get_object_or_404
from django.template import RequestContext

from models import Transacao
from models import Itemagenda
from models import Cliente

from forms import FormItemagenda
from forms import FormCliente
from forms import FormTransacao


def Transacao(request): 
	l_trans = Transacao.objects.all()
	render_to_response("base.html", {'l_trans': l_trans },
		context_instance=RequestContext(request))

def Adctransacao(request):
	if request.method == "POST":
		form = FormTransacao(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return render_to_response("salvo.html", {}, )
	else:
		form = FormTransacao()
	return render_to_response("transacao.html", {'form': form}, 
		context_instance=RequestContext(request))
		

def	Listacli(request):
#	lista_clientes = Cliente.objects.all()
#	return render_to_response("lista.html", {'lista_clientes': lista_clientes },
#		context_instance=RequestContext(request))
	lista_transacao = Transacao.objects.all()
	return render_to_response("lista.html", {'lista_transacao': lista_transacao },
		context_instance=RequestContext(request))

#	lista_itens = Itemagenda.objects.all()
#	return render_to_response("lista.html", {'lista_itens': lista_itens },
#		context_instance=RequestContext(request))

def	Adccliente(request):
	if request.method == "POST":
		form = FormCliente(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return render_to_response("salvo.html", {}, )
	else:
		form = FormCliente()
	return render_to_response("cliente.html", {'form': form}, 
		context_instance=RequestContext(request))
		
			
def Itemagenda(request):
	if request.method == "POST":
		form = FormItemagenda(request.POST, request.FILES) 
		if form.is_valid():
			form.save()
			return render_to_response("salvo.html", {},  )
	else:
		form = FormItemagenda()
	return render_to_response("itemagenda.html", {'form': form }, 
		context_instance=RequestContext(request))


def Detalhe_cli(request, nr_cli):
	try:
		form = Cliente.objects.get(pk=nr_cli)
	except Cliente.DoesNotExist:
		raise Http404(u"Cliente nao existe !")
	return render_to_response("detalhe_cli.html", {'form': form},
		context_instance=RequestContext(request))


def Detalhe_item(request, nr_item):
	form = get_object_or_404(Itemagenda,pk=nr_item)
	return render_to_response("detalhe_item.html", {'form': form},
		context_instance=RequestContext(request))

def Detalhe_trans(request, nr_item):
	form = get_object_or_404(Transacao,pk=nr_item)
	return render_to_response("detalhe_trans.html", {'form': form},
		context_instance=RequestContext(request))


