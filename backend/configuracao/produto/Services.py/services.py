from django.http import HttpResponseRedirect
from .produto.model.models import Produto
from django.shortcuts import get_object_or_404


class ProductsService:
    @staticmethod
    def listarProduto():
        return Produto.objects.all()


        


            
