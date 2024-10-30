from django.db import models

from stdimage.models import StdImageField

class Produtos(models.Model):
    codigo = models.IntegerField('Código Produto', primary_key=True, auto_created=True, unique=True, blank=True)
    nome = models.CharField('Nome Produto', max_length=100, blank=False)
    descricao = models.CharField('Descrição', max_length=100, blank=False)
    quantidade = models.IntegerField('Quantidade', blank=False)
    valor = models.DecimalField('Valor', max_digits=9, decimal_places=2)
    imagem = StdImageField('Imagem', upload_to='produtos', variations={'thumb':(125,125)})

    def __str__(self):
        return self.nome




