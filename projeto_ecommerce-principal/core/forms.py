from django import forms

from .models import Produtos

class ProdutosModelForm (forms.ModelForm):
    class Meta:
        model = Produtos
        fields = ['codigo', 'nome', 'descricao', 'quantidade', 'valor', 'imagem']

