from django.shortcuts import render,HttpResponse,redirect
from .models import User
import bcrypt
from django.contrib import messages
from django.utils.crypto import get_random_string


def index(request):
    return render(request,'app1/index.html')

def registerUser(request):
    if request.method == "POST":
        print(request.POST)
        pw_hash = bcrypt.hashpw(request.POST["pass"].encode(),bcrypt.gensalt())
        
        error = User.objects.basic_validation(request.POST)
        
        if len(error)>0:
            for val in error.values():
                messages.error(request,val)
            return redirect("/")
        else:
            
            hex_store = get_random_string(length = 15)
            # print(hex_store)
            store_user = User.objects.create(first_name=request.POST["first_name"],last_name=request.POST["last_name"],
                                             email=request.POST["email"],password=pw_hash,hexVal=hex_store)
            print(store_user)
            request.session['hex']=hex_store
            # print(request.session['hex'])
            return redirect('/success')
        

def loginUser(request):
    if request.method == "POST":
        print(request.POST)
        
        user = User.objects.filter(email=request.POST["email"])
        
        if user:
            log_user = user[0]
            
            if bcrypt.checkpw(request.POST["pass"].encode(),log_user.password.encode()):
                request.session['hex'] = log_user.hexVal
                return redirect('/success')
            else:
                val = "Invalid Password"
                messages.error(request,val)
                return redirect('/')
        else:
            val = "Invalid Email"
            messages.error(request,val)
            return redirect('/')

def success(request):
    
    try:
        get_user = User.objects.get(hexVal=request.session['hex'])
        
        context = {"first_name":get_user.first_name}
        print(context['first_name'])
        
        return render(request,'app1/success.html',context)
    except:
        return redirect('/')

def destroy(request):
    
    del request.session['hex']
    return redirect('/')
    





#   first_name = models.CharField(max_length=100)
#     last_name = models.CharField(max_length=100)
#     email = models.CharField(max_length=100)
#     password = models.CharField(max_length=255)