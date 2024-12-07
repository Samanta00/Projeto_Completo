from django.http import HttpResponseRedirect
from .produto.model.models import Produto
from django.shortcuts import get_object_or_404


class ProductsService:
    @staticmethod
    def listarProduto():
        return Produto.objects.all()
    @staticmethod
    def obterProduto(product_id):
        return get_object_or_404(Produto, id=product_id)
    
    @staticmethod
    def cadastrarProduto(request):
        if request.method == 'POST':
            nome = request.POST.get('nome')
            preco = request.POST.get('preco')
            quantidade = request.POST.get('quantidade')
            categoria_id = request.POST.get('categoria')
            estoque_minimo = request.POST.get('estoque_minimo')
            estoque_maximo = request.POST.get('estoque_maximo')
            Produto.objects.create(nome=nome, preco=preco, quantidade=quantidade, categoria_id=categoria_id, estoque_minimo=estoque_minimo, estoque_maximo=estoque_maximo)
            return HttpResponseRedirect('/produto/')
        


            
