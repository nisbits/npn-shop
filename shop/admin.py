from django.contrib import admin
from .models import CartItems, CatList,CatWiseItems,contactus

# Register your models her
admin.site.register(CatList )
admin.site.register(CatWiseItems)
admin.site.register(contactus)
admin.site.register(CartItems)


# Register your models here.
