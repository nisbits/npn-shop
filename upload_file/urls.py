from django.contrib import admin
from django.urls import path,include
from . import views



urlpatterns = [
      # path('',views.upload),
      #path("upload_filelis/",views.upload_file),
      #path('lis_/',views.list_view),
      path("upload_image/",views.upload_image),
      path("image_list/",views.image_list,name="image_list"),
      path("mylist/",views.mylist,name="mylist"),
      path("delete/<int:pk>/",views.delete,name="delete"),
      path("edit/<int:pk>/",views.edit,name="edit"),

]

