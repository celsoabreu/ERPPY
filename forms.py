# -*- coding: utf-8 -*-
from django import forms

from models import Cliente
from models import Itemagenda



class FormCliente(forms.ModelForm):
	class Meta:
		model = Cliente

class FormItemagenda(forms.ModelForm):
	class Meta:
		model = Itemagenda
def __str__(self):
        return self.first_name + " " + self.last_name
