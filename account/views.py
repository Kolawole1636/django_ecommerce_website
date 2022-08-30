from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages

# Create your views here.


def login_user(request):
    if request.method=="POST":
        username=request.POST['uname']
        password=request.POST['pass']

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.info(request,"Invalid Credentials")
            return redirect('login')


    return render(request,'login.html')



def register(request):
    if request.method=="POST":
        username=request.POST['uname']
        password1=request.POST['pass1']
        password2=request.POST['pass2']
        email=request.POST['email']
        first_name=request.POST['fname']
        last_name=request.POST['lname']

        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username taken try another one')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email taken try another one')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username,password=password1,email=email,first_name=first_name,last_name=last_name)
                user.save()
                messages.success(request,'Your details have been saved successfully!')
                return redirect('login')
        else:
            messages.error(request,'passwords are not matching check it very well!')
            return redirect('register')




    return render(request,'register.html')


def logout_user(request):
    logout(request)
    return redirect('login')




