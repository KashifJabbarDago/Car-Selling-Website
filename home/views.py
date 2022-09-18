from django.shortcuts import render,HttpResponse,redirect
from django.contrib import messages
from home.models import ContactUs,SignUp
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User 
# Create your views here.

user = authenticate()
def HomePage(request):
    return render(request,'home/Home.html')



def Contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        msg = request.POST['content']

        print(name,email,phone,msg)
        if len(name) < 5 or len(email) < 7 or len(phone) < 5 or len(msg) < 5:
            messages.error(request,'Your form not submitted, hint:Enter minimum 10 character in')
        else:
           contact = ContactUs(name=name,email=email,phone=phone,msg=msg)
           contact.save()
           messages.success(request,'Your form has been submitted successfully, we will contact you shortyl!')
           return redirect('HomePage')
    return render(request,'home/Contact.html')


def signup(request):
    username = request.POST['username']
    first_name = request.POST['fname']
    last_name = request.POST['lname']
    email = request.POST['email']
    password = request.POST['password1']
    password_confirm = request.POST['password2']
    if len(username) > 10:
        messages.error(request,"Form not submitted, Username length should be maximum 10 character")
        return redirect('/')
    
    if password != password_confirm:
        messages.error(request," Form not submitted,Your password one not match to second password confirmation try again")
        return redirect('/')

    myuser = User.objects.create_user(username,email,password)
    myuser.fname = first_name
    myuser.lname = last_name
    myuser.save()
    messages.success(request,"form has been submitted")
    return redirect('/')

def loginhere(request):
    if request.method == "POST":
       login_name = request.POST['loginusername']
       login_pass = request.POST['loginpass']
    user = authenticate(username=login_name,password=login_pass)
    if user is not None:
        login(request,user)
        messages.success(request,"You have logged in successfully! ")
        return redirect('/')
    else:
        messages.error(request,"Invalid credential please try again")
        return redirect('/')

def Logout(request):
    logout(request)
    messages.success(request,"You have successfully logged out!")
    return redirect('/')

def About(request):
        return render(request,'home/About.html')
       