
# from crypt import METHOD_MD5
from email import message
import re
from django.http import HttpResponse , HttpResponseRedirect
from django.shortcuts import render,redirect
from .forms import cat_list_form, cat_wise_items_form,pass_change_form,profile_change_form,user_change_form,pass_forget_form,contactus_form
from .models import CatList as c_list, CatWiseItems,CartItems, OrderItems
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from django.contrib import messages
import random
import string

import razorpay

from fileupload.settings import RAZORPAY_API_KEY,RAZORPAY_API_SECRET_KEY

client = razorpay.Client(auth=(RAZORPAY_API_KEY, RAZORPAY_API_SECRET_KEY))


# Create your views here.
def index(request):
     return render(request,"shop/index.html")  

@login_required(login_url="/shop_accounts/login/")   
def cat_list(request):
    obj=c_list.objects.filter(status=True)
    return render(request,"shop/cat_list.html",{'objects':obj}) 


@login_required(login_url="/shop_accounts/login/")
def add_cat(request):
    if request.method=="POST":
        form=cat_list_form(request.POST)
        if form.is_valid():
           
            form.save()
            print("image saved")
            return redirect("cat_list")
    form=cat_list_form()
    return render(request,"shop/add_cat_form.html",{'form':form})

@login_required(login_url="/shop_accounts/login/")
def deactivate_cat_list(request,pk):
    obj=c_list.objects.get(pk=pk)
    obj.status=False
    obj.save()
    return redirect("cat_list")

@login_required(login_url="/shop_accounts/login/")
def deactivate_cat_wise_item(request,pk):
    obj= CatWiseItems.objects.get(pk=pk)
    obj.status=False
    obj.save()
    
    if request.META['HTTP_REFERER']:
                h=request. META['HTTP_REFERER']
                print(h)
                r=h[-2:-1]
                print(r)
               # return redirect('view_cat_wise_list', pk=r)
                return redirect(h)
    return redirect("cat_list")

    

@login_required(login_url="/shop_accounts/login/")
def view_cat_wise_list(request,pk):
    obj=CatWiseItems.objects.filter(cat=pk,status=True).order_by("item_name")
    if "search" in request.GET:
        search=request.GET["search"]
        obj=CatWiseItems.objects.filter(cat=pk,status=True).filter(Q(item_name__icontains = search)|Q(short_discription__icontains = search))
    
      
       
    
    if "short" in request.GET:
        short=request.GET["short"]
        print(short)
        
        obj=obj.order_by(short)
        
        
    #c=obj.get(cat=pk).cat
    c="c"
    context={'object':obj,"pk":pk,"c_head":c}
    return render(request,'shop/view_cat_wise_item.html',context)

@login_required(login_url="/shop_accounts/login/")
def add_cat_item(request,pk):
    if request.method=="POST":
        form=cat_wise_items_form(request.POST,request.FILES)
        print("above validate")
        if form.is_valid():
            print("catagory:",form.cleaned_data["cat"].pk)
            pk1=form.cleaned_data["cat"].pk
            form.save()
            print("product saved")
            return redirect("view_cat_wise_list",pk1)
    
    form=cat_wise_items_form(initial = {'cat': c_list.objects.get(pk=pk)})
   
    # if request.META['HTTP_REFERER']:
    #             h=request. META['HTTP_REFERER']
    context={"form":form}
    return render(request,"shop/add_cat_item_form.html",context)


def about(request):
    
    return render(request,"shop/about.html")

def contactus(request):
    if request.method=="POST":
        form=contactus_form(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request,'We have got your message, we will contact you soon')
    form= contactus_form()
    context={"form":form}
    return render(request,"shop/contactus.html",context)
    
@login_required(login_url="/shop_accounts/login/")
def single_item_view(request,pk):
    obj= CatWiseItems.objects.get(pk=pk)
    context={"object":obj}
    return render(request,"shop/single_item_view.html",context)

@login_required(login_url="/shop_accounts/login/")
def pass_change(request):
    if request.method=="POST":
        form=pass_change_form(request.POST)
        print("above validate")
        if form.is_valid():
            c_p=form.cleaned_data["confm_pass"]
            p=form.cleaned_data["password"]
            if(c_p==p):
                # user=User.objects.get(id=request.user.id)

                # form.cleaned_data["password"]=hashlib.md5(p.encode("utf-8")).hexdigest()
                print(form.cleaned_data["password"])
                request.user.set_password(form.cleaned_data["password"])
                request.user.save()
                print("password saved")
                return redirect("login")
            else:
                 messages.info(request,'Password did not match')
    form=pass_change_form()
    context={'form':form}  
    return render(request,"shop/pass_change.html",context)
@login_required(login_url="/shop_accounts/login/")
def profile_change(request):
    if request.method == 'POST':
        user_form =user_change_form(request.POST, instance=request.user)
        profile_form = profile_change_form(request.POST, request.FILES, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            # messages.success(request, 'Your profile is updated successfully')
            return redirect(to='shop')
    else:
        user_form =user_change_form(instance=request.user)
        profile_form = profile_change_form(instance=request.user.profile)

    return render(request, 'shop/profile_change.html', {'user_form': user_form, 'profile_form': profile_form})

def pass_forget(request):
    if request.method=="POST":
        form=pass_forget_form(request.POST)
        
        if form.is_valid():
            email=form.cleaned_data["email"]

            if User.objects.filter(email=email).exists()== True:
                obj=User.objects.get(email=email)
                password = ''.join(random.choices(string.ascii_letters +
                             string.digits, k=5))
                obj.set_password(password)
                obj.save()
                print("password changed")
                print(password)
                messages.info(request,'Please check your mail to see your password')
            else:
                messages.info(request,'Email Entered is not registered')
   
    form=pass_forget_form()
    context={"form":form}
    return render(request, 'shop/pass_forget.html',context)


def add_to_cart(request,pk):
    product=CatWiseItems.objects.get(pk=pk)
    cartitem=CartItems.objects.create(user=request.user,product=product)
    return HttpResponseRedirect (request.META.get("HTTP_REFERER"))

def cart(request):
    obj=CartItems.objects.filter(user=request.user)
    total=0
    for product in obj:
       total=total + product.product.price
    print(total)
    contaxt={"cartitems":obj,"total":total}
    return render(request, 'shop/cart.html',contaxt)

def checkout_cart(request):
    obj=CartItems.objects.filter(user=request.user)
    total=0
    for product in obj:
       total=total + product.product.price
    print(total)
    contaxt={"cartitems":obj,"total":total}
    return render(request, 'shop/checkout.html',contaxt)

def checkout_single_item(request,pk):
     product=CatWiseItems.objects.get(pk=pk)
     contaxt={"product":product,"total":product.price,"pk":pk}
     return render(request, 'shop/checkout.html',contaxt)

def place_order(request):
    items=CartItems.objects.filter(user=request.user)
    total=0
    for item in items:
        obj=OrderItems.objects.create(
            user=request.user,
            product=item.product
            
        )
        total= total+item.product.price
    obj.save()
    items.delete()
    #################### payment process ######################
    order_amount = total *100
    order_currency = "INR"

    # order_receipt = "order_rcptid_11"

    # notes = {'Shipping address':'Bommanahalli, Bangalore'}
    # client.order.create(amount=order_amount, currency=order_currency, receipt=order_receipt, notes=notes)
    payment_order=client.order.create(dict(amount=order_amount, currency=order_currency, payment_capture=1))
    payment_order_id=payment_order["id"]
    methods=['card',
            'netbanking',
            'wallet',
            'emi',
            'upi',]
    method=random.choice(methods)
    method="card"
    context={"amount":500, "api_key":RAZORPAY_API_KEY,"order_id":payment_order_id,"method":method }
    return render(request,"shop/pay.html",context)


    messages.success(request,"you have successfully ordered")
    # return HttpResponse("<h1>You have sucessfully ordered</h1>")
    return redirect(request.META['HTTP_REFERER'])

def single_place_order(request,pk):
    product=CatWiseItems.objects.get(pk=pk)
    obj=OrderItems.objects.create(
            user=request.user,
            product=product
            
        )
    obj.save()
    #################### payment process ######################
     

    order_amount = product.price *100
    order_currency = "INR"

    # order_receipt = "order_rcptid_11"

    # notes = {'Shipping address':'Bommanahalli, Bangalore'}
    # client.order.create(amount=order_amount, currency=order_currency, receipt=order_receipt, notes=notes)
    payment_order=client.order.create(dict(amount=order_amount, currency=order_currency, payment_capture=1))
    payment_order_id=payment_order["id"]
    methods=['card',
            'netbanking',
            'wallet',
            'emi',
            'upi',]
    method=random.choice(methods)
    method="card"
    context={"amount":500, "api_key":RAZORPAY_API_KEY,"order_id":payment_order_id,"method":method }
    return render(request,"shop/pay.html",context)
    messages.success(request,"you have successfully ordered")
    # return HttpResponse("<h1>You have sucessfully ordered</h1>")
    return redirect(request.META['HTTP_REFERER'])

def myorders(request):
    orders=OrderItems.objects.filter(user=request.user)
    context={"orders":orders}
    return render(request, 'shop/my_orders.html',context)
