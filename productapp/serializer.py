from rest_framework import serializers
from .models import productMainModel,productColourModel,productImageModel


class productColourserializer(serializers.ModelSerializer):
    class Meta:
        model = productColourModel
        fields = "__all__"



class proproductImageserialzer(serializers.ModelSerializer):
    class Meta:
        model = productImageModel
        fields = "__all__"

class productSerializer(serializers.ModelSerializer):
    product_details = productColourserializer(read_only=True,many=True)
    product_img_details = proproductImageserialzer(read_only=True,many=True)
    class Meta:
        model = productMainModel
        fields = "__all__"

