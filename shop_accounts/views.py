from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth,Group
from django.http import HttpResponse
from django.contrib import messages
from django.utils import timezone
from .models import profile

# Create your views here.
def login ( request ) :
   
    print("this is, next=",request.GET.get('next'))
    if request.method == 'POST' :
       username = request . POST [ 'username' ]
       password = request . POST [ 'password' ]
       user = auth.authenticate( username=username , password = password)
       if user is not None :
           auth.login (request,user )
           print("valid user")
           uname=request.user.get_username()
           if len(uname)>8:
                    uname=uname[0:7]
                    uname=uname+".."
           request.session['uname']=uname
           nm=request.session['uname']
           print(nm)
         
           #print(request. META['HTTP_REFERER'])
          
           """if request. META['HTTP_REFERER']:
                h=request. META['HTTP_REFERER']
                r=h.split("=")
                print(r)
                print("have a next parameter")
                return redirect (r[1]) """
           if request.POST.get("next"):
                print(request.POST.get("next")) 
               
             
                return redirect (request.POST.get("next"))
    
          
           return redirect ( "shop" )

           
       else :
            print("invalid user")
            messages.info ( request , ' invalid credentials ' )
            return redirect( 'login' )
    return render ( request , 'shop/login.html' )


def index(request):
   
    return render(request,'fileupload/home.html')
def register(request):
    if request.method == "POST":
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST["username"]
        password1=request.POST["password1"]
        password2=request.POST['password2']
        email=request.POST['email']

        if password1==password2:
            if User.objects.filter(username=username).exists():
                 print("user already exist")
                 messages.info(request,'user already exist')
                 return redirect("register")
            elif User.objects.filter(email=email).exists():
                print("email taken")
                messages.info(request,'email already exist')
                return redirect("register")
            else:
                user=User.objects.create_user( last_login=timezone.now(),username=username,password=password1,email=email,first_name=first_name,last_name=last_name)
                user.save()
                pro=profile.objects.create(user=user)
                pro.save()
                group = Group.objects.get(name='customer')
                user.groups.add(group)

                print("user created")
                return redirect("login")
               
        else:
            print("password don't match")
            messages.info(request,"password don't match")
            return redirect("register")
    else:
        return render(request,"shop/registration.html")    


def logout(request):
    auth.logout(request)
    return redirect("shop")

def about(request):
    
    return render(request,"shop/about.html")

def contactus(request):
    
    return render(request,"shop/contactus.html")
    

def test(request):
    
    return render(request,"shop/test.html")