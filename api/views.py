from rest_framework.response import Response
from rest_framework import generics
from rest_framework.views import APIView
from django.http import Http404
from django.forms.models import model_to_dict

from .models import Product
from .serializers import CreateProductSerializer


# class ProductCreateView(APIView):
#     """Creating APIView for product"""
#
#     def post(self, request):
#         product = CreateProductSerializer(data=request.data)
#         if product.is_valid():
#             product.save()
#         return Response(status=201)


class ProductAPIView(APIView):
    # get, post, put, patch, delete
    # def get_object(self, pk):
    #     try:
    #         return Product.objects.get(pk=pk)
    #     except Product.DoesNotExist:
    #         raise Http404

    # def get(self, request):
    #     products = Product.objects.all()
    #     return Response({'info': model_to_dict(products)})

    def post(self, request):
        product = Product.objects.create(
            title=request.data.get('title'),
            price=request.data.get('price')
        )
        return Response({'text': model_to_dict(product)})

    # def put(self, request):