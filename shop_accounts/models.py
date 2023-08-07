from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class profile(models.Model):
    user=models.OneToOneField(User, null=True,on_delete=models.CASCADE)
    pro_pic=models.ImageField(upload_to="shop/pro_pic/",default="shop/pro_pic/pro_icon.jpg",null=True,blank=True)
    pubilsh_date=models.DateTimeField( auto_now_add=True,null=True)
    update_date=models.DateTimeField( auto_now_add=True,null=True)

    def __str__ ( self ):
        return str(self.user)