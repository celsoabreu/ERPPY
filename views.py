# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response, render, get_object_or_404
from django.template import RequestContext
from django.http import Http404


from models import Itemagenda
from forms import FormItemagenda

from models import Cliente
from forms import FormCliente


def transacao(request): 
	if request.method =='POST':
		transacao = request.POST.get('transacao')
		template = request.POST.get('template')
		n_contato = Contat(
			transacao=transacao,
			template=template, 
		)
		n_contato.save()
	else:
		transacao = ''
		templates =  ''
		
	return render( request, 'base.html', 
		{	'Transacao': transacao,
		     'Template': template,
		}
	)



def	listacli(request):
	lista_clientes = Cliente.objects.all()
	return render_to_response("lista.html", {'lista_clientes': lista_clientes },
		context_instance=RequestContext(request))
	lista_itens = Itemagenda.objects.all()
	return render_to_response("lista.html", {'lista_itens': lista_itens },
		context_instance=RequestContext(request))


def	adccliente(request):
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
		form = Itemagenda(request.POST, request.FILES)
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
	item = get_object_or_404(Itemagenda,pk=nr_item)
	return render_to_response("detalhe_item.html", {'item': item},
		context_instance=RequestContext(request))

