from django.forms import ModelForm
from .models import recipebookapp
from django import forms

class CreateRecipeForm(ModelForm):
    class Meta:
        model = recipebookapp
        fields = "__all__"
        widgets = {'ingredient':forms.Textarea(),'How_to_make':forms.Textarea(),
                   'created_by':forms.HiddenInput()}