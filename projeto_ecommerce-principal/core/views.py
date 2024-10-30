from django.shortcuts import render, redirect

from .forms import ProdutosModelForm

from django.http import HttpResponse

from django.contrib import messages

from .models import Produtos

def consultaprodutos(request):
    context = {
        'produtos': Produtos.objects.all()
    }
    return render(request, 'consultaprodutos.html', context)

def index(request):
    return render(request, 'index.html')

def contato(request):
    return render(request, 'contato.html')

def produtos(request):
    #print(f'Usuário:{request.user}')
    if str(request.user) !='AnonymousUser':   #se for diferente de usuário anônimo executa o POST
        if request.method == 'POST':
            form = ProdutosModelForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                messages.success(request, 'Produto Salvo com sucesso.')
                #return HttpResponse('Dados enviados com sucesso')
                form = ProdutosModelForm()
            else:
                messages.error(request, 'Erro ao salvar o produto')
                #return HttpResponse('Os Dados não foram enviados')
        else:
            form = ProdutosModelForm()
        context = {
            'form': form
        }
        return render(request, 'produto.html', context)
    else:
        return redirect('/admin/login/?next=/admin/') #se usuário igual anônimo
        #return render(request, 'index.html')
