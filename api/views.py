from rest_framework.response import Response
from rest_framework import generics
from rest_framework.views import APIView
from django.http import Http404
from django.forms.models import model_to_dict

from .models import Product
from .serializers import CreateProductSerializer


class ProductAPIView(APIView):
    # get, post, put, patch, delete

    def get(self, request, pk):
        product = Product.objects.get(pk=pk)
        return Response({'text': model_to_dict(product)})

    def post(self, request):
        product = Product.objects.create(
            title=request.data.get('title'),
            price=request.data.get('price')
        )
        return Response({'text': model_to_dict(product)})

    def put(self, request, pk):
        product = Product.objects.get(pk=pk)
        product.title = request.data.get('title')
        product.price = request.data.get('price')
        product.save()
        return Response({'text': model_to_dict(product)})

    def patch(self, request, pk):
        product = Product.objects.get(pk=pk)
        if request.data.get('title'):
            product.title = request.data.get('title')
        else:
            product.price = request.data.get('price')
        product.save()
        return Response({'text': model_to_dict(product)})

    def delete(self, request, pk):
        product = Product.objects.get(pk=pk)
        product.delete()
        return Response({'text': 'object deleted'})
