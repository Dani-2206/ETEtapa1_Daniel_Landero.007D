from abc import abstractstaticmethod
from typing import AbstractSet
from django import forms
from django.db import models
from django.db.models import fields
from django.db.models.query import prefetch_related_objects
from django.forms import ModelForm,Widget, widgets
from . models import periodista

class formu_p(ModelForm):
   
    class Meta:
        model = periodista
        fields = ['rut','foto','nombre_c','telefono','direccion','email','pais','contrasena']
        widgets ={
            'rut': 'Rut',
            'foto': 'Foto',
            'nombre_c': 'Nombre Completo',
            'telefono': 'Telefono',
            'direccion': 'Direccion',
            'email': 'Email',
            'pais': 'Pais',
            'contrasena': 'contrasena'
        }

        widgets ={
            'rut': forms.TimeInput(
                attrs ={
                    'class':'form-control',
                    'name':'rut',
                    'placeholder':'12345678-9',
                    'min_lenght':'10'           
                }
            ),
            'foto': forms.FileInput,
            'nombre_c': forms.TextInput(
                attrs={
                    'class':'form-control',
                    'min_lenght':'40',
                    'placeholder':'Fulanito marcelo sabal aguilera',
                    'name':'nombre'
                }
            ),
            'telefono': forms.NumberInput(
                attrs={
                    'class':'form-control',
                    'min_lenght':'9',
                    'name':'telefono'
                }
            ),
            'direccion': forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'jose miguel 1234',
                    'name':'direccion'
                }
            ),
            'email': forms.TextInput(
                attrs= {
                    'class':'form-control',
                    'placeholder':'fulanito@gmail.com',
                    'name':'email'
                }
            ),
            'pais': forms.Select(
                attrs={
                    'name':'pais',
                    'class':'form-control'
                }
            ),
            'contrasena':forms.PasswordInput(
                attrs={
                    'class':'form-control',
                    'name':'contrasena',
                    'min_lenght':'5'

                }

            )


        }


