from django.contrib import admin

# Register your models here.
#b
from .models import Produtos,Cliente

admin.site.register(Produtos)
admin.site.register(Cliente)

"""admin.site.register(Cliente)
@admin.register(Produto)"""

class ProdutosAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'nome', 'descricao', 'quantidade', 'valor', 'imagem')
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('cpf', 'nome', 'data_nascimento', 'email', 'telefone', 'codigo_produto')    

