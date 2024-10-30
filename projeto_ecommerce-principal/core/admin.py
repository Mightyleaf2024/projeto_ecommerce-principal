from django.contrib import admin

# Register your models here.
#b
from .models import Produtos

admin.site.register(Produtos)

"""admin.site.register(Cliente)
@admin.register(Produto)"""

class ProdutosAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'nome', 'descricao', 'quantidade', 'valor', 'imagem')

