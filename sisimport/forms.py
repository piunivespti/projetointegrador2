from django import forms

from .models import produto

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = produto
        fields = '__all__'

