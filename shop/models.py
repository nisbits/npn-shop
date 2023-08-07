from email.policy import default
from tkinter import CASCADE
from unicodedata import category
from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class CatList( models.Model ) :
    category_name= models.CharField ( max_length = 15,unique=True )
    status=models.BooleanField(default=True)
    def __str__ ( self ) :


        return self.category_name

# catg=[]
# obj=CatList.objects.all()
# for o in obj:
#     t=(CatList.objects.get(pk=o.pk),o.category_name)    
#     catg.append(t)
#     print(t)
# # catg = (
# #     ('1','electronics'),
# #     ('2','cloths'),
# #     ('kids','3'),
# #     ('kitchen','4'),
# #     ('cat','5'),
# #)
# catg=tuple(catg)
class CatWiseItems(models.Model):
    cat =  models.ForeignKey(CatList, max_length = 100, on_delete=models.CASCADE)
    item_name= models.CharField (max_length = 100)
    short_discription=models.TextField(max_length=100)
    long_discription=models.TextField(max_length=255)
    image=models.ImageField(upload_to="shop/")
    specs=models.TextField(max_length=100)
    price=models.IntegerField()
    status=models.BooleanField(default=True)
    upload_date= models.DateTimeField( auto_now_add=True)
   
    def __str__ ( self ) :
        return self.item_name


class contactus(models.Model):
    name=models.CharField(max_length = 100)
    email=models.EmailField()
    phone_no=models.CharField(max_length = 10)
    subject=models.CharField(max_length = 100)
    message=models.TextField(max_length=255)
    submit_date= models.DateTimeField( auto_now_add=True)
    

    def __str__ ( self ) :
        return str(self.user)



    
class CartItems(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    product=models.ForeignKey(CatWiseItems, on_delete=models.SET_NULL, null=True, blank=True)
    
    def __str__ ( self ):
        return str(self.user)

class OrderItems(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    product=models.ForeignKey(CatWiseItems, on_delete=models.SET_NULL, null=True, blank=True)
    order_date=models.DateField( auto_now_add=True )
    order_status=models.CharField( max_length=50,default="Pending")
    
    payment_method=models.CharField(default="COD",max_length=50)
    def __str__ ( self ):
        return str(self.user)