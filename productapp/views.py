from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView , RetrieveAPIView
from .serializer import productSerializer ,productColourserializer , proproductImageserialzer
from .models import productMainModel , productColourModel , productImageModel
# Create your views here.


class productView(ListCreateAPIView):
    queryset = productMainModel.objects.all()
    serializer_class = productSerializer

class getsingleproduct(RetrieveAPIView):
    queryset = productMainModel.objects.all()
    serializer_class = productSerializer


class colorView(ListCreateAPIView):
    queryset = productColourModel.objects.all()
    serializer_class = productColourserializer

class imageView(ListCreateAPIView):
    queryset = productImageModel.objects.all()
    serializer_class = proproductImageserialzer
