import random

from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Product, User
from .serializers import ProductSerializer

class ProductViewSet(viewsets.ViewSet):

    def list(self, request):
        # GET /api/products
        products = Product.objects.all()
        serializer = ProductSerializer(instance=products, many=True)
        reponse_data = Response(serializer.data)
        return reponse_data


    def create(self, request):
        # POST /api/products
        serializer = ProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        response_data = Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return response_data

    def retrieve(self, request, pk=None):
        # GET /api/products/<str:id>
        product = Product.objects.get(id=pk)
        serializer = ProductSerializer(instance=product)
        response_data = Response(data=serializer.data)
        return response_data

    def update(self, request, pk=None):
        # PUT /api/products/<str:id>
        product = Product.objects.get(id=pk)
        serializer = ProductSerializer(instance=product, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        response_data = Response(data=serializer.data, status=status.HTTP_202_ACCEPTED)
        return response_data

    def destroy(self, request, pk=None):
        # DELETE /api/products/<str:id>
        product = Product.objects.get(id=pk)
        product.delete()
        response_data = Response(status=status.HTTP_204_NO_CONTENT)
        return response_data


class UserAPIView(APIView):
    def get(self, _):
        users = User.objects.all()
        user = random.choice(users)
        return Response({
            'id': user.id
        })

