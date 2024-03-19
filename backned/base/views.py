from urllib import response
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import status
from rest_framework.response import Response
from .serializers import ProductSerializer
from django.http import JsonResponse
from django.views import View
from .models import Product
from rest_framework.decorators import api_view


@api_view(['GET','POST','DELETE','PUT','PATCH'])
def Products(req,id=-1):
    if req.method =='GET':
        if id > -1:
            try:
                temp_Product=Product.objects.get(id=id)
                return Response (ProductSerializer(temp_Product,many=False).data)
            except Product.DoesNotExist:
                return Response ("not found")
        all_Products=ProductSerializer(Product.objects.all(),many=True).data
        return Response ( all_Products)
    if req.method =='POST':
        tsk_serializer = ProductSerializer(data=req.data)
        if tsk_serializer.is_valid():
            tsk_serializer.save()
            return Response ("post...")
        else:
            return Response (tsk_serializer.errors)
    if req.method =='DELETE':
        try:
            temp_Product=Product.objects.get(id=id)
        except Product.DoesNotExist:
            return Response ("not found")    
       
        temp_Product.delete()
        return Response ("del...")
    if req.method =='PUT':
        try:
            temp_Product=Product.objects.get(id=id)
        except Product.DoesNotExist:
            return Response ("not found")
       
        ser = ProductSerializer(data=req.data)
        old_Product = Product.objects.get(id=id)
        res = ser.update(old_Product, req.data)
        return Response('upd')

class GetImages(View):
    def get(self, request):
        res = [] #create an empty list
        for img in Product.objects.all(): #run on every row in the table...
            res.append({
                "title": img.title,
                "description": img.description,
                "completed": False,
                "image": str(img.image)
            }) #append row by row to res list
        return JsonResponse(res, safe=False)

class APIViews(APIView):
    parser_class=(MultiPartParser,FormParser)
    def post(self,request,*args,**kwargs):
        api_serializer=ProductSerializer(data=request.data)
        if api_serializer.is_valid():
            api_serializer.save()
            return Response(api_serializer.data,status=status.HTTP_201_CREATED)
        else:
            print('error',api_serializer.errors)
            return Response(api_serializer.errors,status=status.HTTP_400_BAD_REQUEST)


# class Products(View):
#     def get(self, request, *args, **kwargs):
#         all_products = ProductSerializer(Product.objects.all(), many=True).data
#         return JsonResponse(all_products, safe=False)

#     def post(self, request, *args, **kwargs):
#         # Handle POST request here
#         data = {
#             'message': 'POST request received'
#         }
#         return JsonResponse(data)