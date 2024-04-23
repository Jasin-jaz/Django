from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view, APIView
from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework import status


# -------------Category----------------- #
@api_view(['GET','POST'])
def category_list(request):
    if request.method == 'GET':
        category = Category.objects.all()
        serializer = CategorySerializer(category, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    elif request.method == 'POST':
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
# ------------------Product----------------#
@api_view(['GET','POST'])
def product_list(request):
    if request.method == 'GET':
        product = Product.objects.all()
        serializer = ProductSerializer(product, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    elif request.method == 'POST':
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  
    
# -------------------ProductVariant-------------#
@api_view(['GET','POST'])
def productvar_list(request):
    if request.method == 'GET':
        productvar = ProductVariant.objects.all()
        serializer = ProductVariantSerializer(productvar, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    elif request.method == 'POST':
        serializer = ProductVariantSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
# ------------------Category view by id  
@api_view(['GET'])
def category_view(request, category_id):
    category = Category.objects.get(id=category_id)
    if request.method == 'GET':
        serializer = CategorySerializer(category)
        return Response(serializer.data, status.HTTP_200_OK)
    
# -------------------Product view by id
@api_view(['GET'])
def product_view(request, product_id):
    product = Product.objects.get(id=product_id)
    if request.method == 'GET':
        serializer = ProductSerializer(product)
        return Response(serializer.data, status.HTTP_200_OK)

# -------------------ProductVariants view by id
@api_view(['GET'])
def productvar_view(request, productvar_id):
    productvar = ProductVariant.objects.get(id=productvar_id)
    if request.method == 'GET':
        serializer = ProductVariantSerializer(productvar)
        return Response(serializer.data, status.HTTP_200_OK)
    
# --------------------Category with product and product with productvariants
class CategoryWithProduct(APIView):
    def get(self, request, category_id, format=None):
        try: 
            category = Category.objects.get(id=category_id)
        except Category.DoesNotExist:
            return Response({'error':'Category not found'}, status=status.HTTP_404_NOT_FOUND) 
        category_serializer = CategorySerializer(category)
        products = Product.objects.filter(category=category)

        product_data = []
        for product in products:
            product_serializer = ProductSerializer(product)
            products_var = ProductVariant.objects.filter(product=product)
            productvar_serializer = ProductVariantSerializer(products_var, many=True)
            product_data.append({
                'product': product_serializer.data,
                'variants': productvar_serializer.data
            })        

        response_maindata = {
            'category': category_serializer.data,
            'All products & its variants of the selected category': product_data
        }

        return Response(response_maindata, status=status.HTTP_200_OK)
    
# class CategoryWithProduct(APIView):
    # def get(self, request, category_id, format=None):
        # try: 
        #     category = Category.objects.get(id=category_id)
        # except Category.DoesNotExist:
        #     return Response({'error':'Category not found'}, status=status.HTTP_404_NOT_FOUND) 
        # category_serializer = CategorySerializer(category)
        # products = Product.objects.filter(category=category)
        # product_serializer = ProductSerializer(products, many=True)
        # products_var = ProductVariant.objects.filter(product__in=products)
        # productvar_serializer = ProductVariantSerializer(products_var, many=True)
        # response_data = {
        #     'products' : product_serializer.data,
        #     'products_var' : productvar_serializer.data,
        # }
        # response_maindata = {
        #     'category' : category_serializer.data,
        #     'response_details' : response_data,
        # }
        # return Response(response_maindata, status=status.HTTP_200_OK)
















