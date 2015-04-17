# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _


class Transacao  (models.Model):
	transacao = models.CharField( _('Transacao'), max_length=45,  help_text='Nome da Transacao')
	template =  models.CharField( _('Template'), max_length=100,  help_text='Caminho do template')

	class Meta:
		db_table = 'transacao'
		verbose_name = 'Transação'
		verbose_name_plural = 'Transações'


class Ativ_economica  (models.Model):
	atividade = models.CharField( _('Ativ economica'), max_length=45,  help_text='Nome da atividade economica')

	class Meta:
		db_table = 'ativ_economica'
		verbose_name = 'Ativ_Economica'
		verbose_name_plural = 'Ativ_Economicas'

class Inscr_municipal(models.Model):
	codigo =  models.CharField(max_length=20, verbose_name='Insc. Municipal', help_text='Codigo da Inscrição Municipal')
	Descricao =  models.CharField(max_length=45, verbose_name='Descrição', help_text='Descricao da Inscrição Municipal')
	
	class Meta:
		db_table = 'inscr_municipal'
		verbose_name = 'Inscr. Municipal'
		verbose_name_plural = 'Inscr. Municipal'
		
class Inscr_estadual(models.Model):
	codigo =  models.CharField(max_length=20, verbose_name='Insc. Estadual', help_text='Codigo da Inscrição Estadual')
	Descricao =  models.CharField(max_length=45, verbose_name='Descrição', help_text='Descricao da Inscrição Estadual')
	
	class Meta:
		db_table = 'inscr_estadual'
		verbose_name = 'Inscr. Estadual'
		verbose_name_plural = 'Inscr. Estadual'
		
		
class Cliente(models.Model):
	nome = models.CharField(max_length=100, verbose_name='Nome')
	cpf = models.CharField(max_length=20, verbose_name='CPF')
	email = models.EmailField(max_length=75, verbose_name='Email')
	celular = models.CharField(max_length=15, verbose_name='Celular')
	
	class Meta:
		db_table = 'cliente'
		verbose_name = 'Cliente'
		verbose_name_plural = 'Clientes'
	
	def __unicode__(self):
		return self.nome + " " + self.cpf
		
class Itemagenda(models.Model):
	cliente =  models.ForeignKey('Cliente', verbose_name = 'Cliente')
	titulo = models.CharField(max_length=50, verbose_name='Titulo')
	descricao = models.TextField(max_length=1024, verbose_name='Assunto')
	data = models.DateField()
	hora = models.TimeField()
		
	class Meta:
		db_table = 'itemagenda'
		verbose_name = 'Itemagenda'
		verbose_name_plural = 'Itemagendas'
	
	def __unicode__(self):
		return self.cliente + " " + self.titulo + " " + self.data + " " + self.hora
