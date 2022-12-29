from django.db import models

class productMainModel(models.Model):
    Title = models.CharField(max_length=100)
    Description = models.TextField()
    price = models.IntegerField()
    unique_code = models.CharField(max_length=80,unique=True)
    size = models.CharField(max_length=100) 
    quality = models.CharField(max_length=100)

class productColourModel(models.Model):
    Product = models.ForeignKey(productMainModel,on_delete=models.CASCADE,related_name='product_details')
    Colour = models.CharField(max_length=100)

class productImageModel(models.Model):
    Product = models.ForeignKey(productMainModel,on_delete=models.CASCADE,related_name='product_img_details')
    Image = models.ImageField(upload_to='images')



    