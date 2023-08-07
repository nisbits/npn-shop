from ast import Pass
from http.client import HTTPResponse
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
from openpyxl import Workbook,load_workbook
from openpyxl.utils import  get_column_letter

from upload_file.models import uploaded_image
from .forms import imageform,imageform_update
import datetime
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.

'''def upload(request):
    if request.method =='POST':
        nn= request.POST["nn"]
        uploaded_file=request.FILES["document"]
        
        print(uploaded_file)
      
        print(uploaded_file.name)
        print(uploaded_file.size)
        print("helo")
        
        fs=FileSystemStorage()
        global name
        name=fs.save(uploaded_file.name,uploaded_file)
        print(name )
        #process()
        url=fs.url("output.xlsx")
        print(url)
        context={'url':url}
        return render(request,"upload.html",context)
    return render(request,"upload.html")'''


'''def upload_file(request):
    if request.method== "POST":
        file_name = request . POST [ 'file_name' ]
        author = request . POST [ 'author' ]
        pdf=request.FILES["file"]
        print(pdf)
        q=uploaded_file.objects.create(file_name=file_name,author=author,pdf=pdf)
        q.save()
        return redirect("/upload/lis_/")
        
    return render(request,"upload_forlis.html")'''

'''
def list_view(request):
    object=uploaded_file.objects.all()  
    return render(request,"list_view.html",{"object":object})
'''
@login_required(login_url="/acounts/login/")
def upload_image(request):
    if request.method=="POST":
        form=imageform(request.POST,request.FILES)
        if form.is_valid():
            instance=form.save(commit=False)
            instance.user=request.user
            instance.save()
            print("image saved")
            return redirect("image_list")
    else:
        form=imageform()
        context={"form":form}
    return render(request,"fileupload/upload_image.html",context)
@login_required(login_url="/acounts/login/")    
def image_list(request):
    object=uploaded_image.objects.all()  
    
    return render(request,"fileupload/image_list.html",{"objects":object})
    
def test(request):
    return render(request,"up.html")
@login_required(login_url="/acounts/login/")   
def mylist(request):
     object=uploaded_image.objects.filter(user=request.user.id)  
     print(request.user)
     print(request.user.id)
     return render(request,"fileupload/mylist.html",{"objects":object})
      

@login_required(login_url="/acounts/login/")  
def delete(request,pk):
    if request.method== 'POST' :
     file_obj= uploaded_image.objects.get(pk=pk)
     file_obj.delete()
    return redirect ("mylist")

@login_required(login_url="/acounts/login/")
def edit(request,pk):
    r=uploaded_image.objects.get(pk=pk)
    if r.user==request.user:
        if request.method=="POST":
            form=imageform_update(request.POST,request.FILES)
            if form.is_valid():
            # print("valid upload form")
            # img_name= form.cleaned_data['image_name']
            # img= form.cleaned_data['image']
            # q=uploaded_image.objects.get(pk=pk)
            # q.image_name=img_name
            # q.image=img
            # q.save()
                form=imageform_update(request.POST,request.FILES,instance=r)
                form.save()
                return redirect("mylist")

   
        form=imageform_update(instance=r)
        context={"form":form}
        return render(request,"fileupload/update_image.html",context)
    else:
        return redirect ("/")

        
    