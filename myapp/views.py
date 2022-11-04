from django.shortcuts import render
from .models import *

# Create your views here.
def index(request):
    return render(request,'index.html')

#View for register user
def UserRegister(request):
        if request.method == "POST":
            fname=request.POST['fname']
            lname=request.POST['lname']
            email=request.POST['email']
            contact=request.POST['contact']
            password=request.POST['password']
            cpassword=request.POST.get('cpassword','default_value')
            

            #First we will validate that user already exist
            user=User.objects.filter(Email=email)    

            if user:
                message = "User Already Exist"       
                return render(request,"index.html",{'msg':message})
            else:
                if password==cpassword:
                  newuser=User.objects.create(Firstname=fname,Lastname=lname,Email=email,Contact=contact,Password=password)
                  message = "User Successifully Registered" 
                  return render(request,"login.html",{'msg':message})
                else:
                    message = "Password and confirm password doesnot match"
                    return render(request,"index.html",{'msg':message})
def LoginPage(request):
      return render(request,'login.html')

def LoginUser(request):
    if request.method == "POST":
            email=request.POST['email']
            password=request.POST['password']
            #checking the email with database
            user=User.objects.get(Email=email)
            if user:
                if user.Password==password:
                    #Fetching information into session from database
                    request.session['Firstname']=user.Firstname
                    request.session['Lastname']=user.Lastname
                    request.session['Email']=user.Email
                    request.session['Contact']=user.Contact
                    return render(request,'home.html')   

                else:
                    message="Password does not match"
                    return render(request,'login.html',{'msg':message})
            else:
                message="User does not exist " 
                return render(request,'register.html',{'msg':message})      


                
                

