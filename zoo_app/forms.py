from django import forms
from .models import *


class CreateAviaryForm(forms.ModelForm):
    class Meta:
        model = Aviary
        fields = ('name','description', 'type', 'img',)


class CreateAnimaliaForm(forms.ModelForm):
    class Meta:
        model = Animalia
        fields = ('name','description', 'area', 'type', 'img',)


class CreateAnimalForm(forms.ModelForm):
    class Meta:
        model = Animal
        fields = ('AnimaliaType', 'name','description', 'img',)



