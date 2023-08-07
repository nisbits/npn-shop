from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from django.utils import timezone
from datetime import timedelta,datetime

ist_time = datetime.now() + timedelta(hours=5,minutes=30)




class uploaded_image( models.Model ) :
    image_name = models.CharField ( max_length = 100 )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.FileField( upload_to ="image",max_length=100 )
    upload_date= models.DateTimeField( auto_now_add=True)
    def __str__ ( self ) :
        return self.image_name
    def delete ( self , *args , **kwargs ) :
        self.image.delete()
        
        super().delete( *args ,**kwargs )    