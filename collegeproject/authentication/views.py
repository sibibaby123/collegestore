from django.contrib import auth , messages
from django.contrib.auth import authenticate , login
from django.shortcuts import render , redirect
from django.contrib.auth.models import User
from django.urls import reverse
from .models import Department,Purpose, UserExtra
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from .models import Collegepart,CollegepartImage
from django.http import HttpResponse
from django.contrib import messages
import uuid
import re
# Create your views here.

def register(request):
    if request.method == "GET":
        return  render(request, "registration.html")
    elif request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        c_password = request.POST.get('cpassword')
        user = User.objects.filter(username = username)
        if(len(user)!=0):
            error = "Username already exist!"
            return render(request ,"registration.html",{"error" : error})
        user = User.objects.filter(email = email)
        if (len(user)!= 0):
            error = "Email already exist!"
            return render(request ,"registration.html",{"error" : error})
        if password == c_password:
            user = User(first_name=first_name,last_name=last_name,username=username,email=email)
            user.set_password(password)

            if re.match( r'^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[@#$%^&+=])[\w\d@#$%^&+=]{8,}$' , password):
                print("Valid password")
            else :
                print("Password not valid")
                return render(request,"registration.html",{'error':"password not valid"})
            user.save()
            print("user created successfully")
            return redirect('/')
        else:
            error = "Not matching"
            return render(request, "registration.html", {"error": error})

def login_page(request):
    if request.method == 'GET':
        context={}
        return render(request,'login.html',context)
    else:
        if request.method == 'POST':
           username=request.POST['username']
           password=request.POST['password']
           myuser=authenticate(request,username=username,password=password)
           if myuser is not None:
              login(request,myuser)
              return redirect("home/")
           else:
                context= {
                    'error':"invalid username or password"
                         }
                return render(request,"login.html",context)

def logout(request):
    auth.logout(request)
    return redirect('/')
def dataform(request):
    try:
        data = UserExtra.objects.get(user=request.user)
    except:
        data = None
    if request.method == "GET":
        context = {
            "userextra": data
        }
        return render ( request , "dataform.html", context)
    elif request.method == "POST":
        date=request.POST['date']
        age=request.POST['age']
        gender = request.POST['inlineRadioOptions']
        number = request.POST['number']
        address = request.POST['address']
        if(data is None):
            userextra = UserExtra(
                user = request.user,
                age = age,
                dateofbirth = date,
                gender = gender,
                phonenumber = number,
                address = address
            )
            userextra.save()
        else:
            data.age = age
            data.dateofbirth=date
            data.gender = gender
            data.phonenumber=number
            data.address=address
            data.save()
        return redirect("/home/")

def allCourse(request):
    links=Department.objects.all()
    return render(request,"home.html",{'links':links})


def department(request,slug):
    department=Department.objects.get(slug=slug)
    print(department)
    return render(request,"department.html",{'department':department})

def enquiry(request,slug="enquiry"):
    if request.method == "GET" :
        context = {
            "department":Department.objects.all()
        }
        return render(request ,"enquiry.html", context)
    elif request.method == "POST" :
        title = request.POST.get('title')
        dept = request.POST.get('department')
        desc = request.POST.get('comments')
        purpose = Purpose(
                name=title,
                user = request.user,
                slug = str(uuid.uuid4())[:10],
                department_id=dept,
                desc= desc,
            )
        purpose.save()
        return render(request,"success.html",{'purpose':purpose})

def placeorder(request,slug="place-order"):
    if request.method == "GET":
        context={
            'department':Department.objects.all()
        }
        return render(request,"placeorder.html",context)
    elif request.method == "POST":
        title = request.POST.get('title')
        dept = request.POST.get('department')
        desc=request.POST.get('comments')
        item_pen_no = request.POST.get('pens',0)
        item_book_no = request.POST.get('books',0)
        item_paper_no = request.POST.get('papers',0)
        purpose = Purpose(
                 name=title,
                 user = request.user,
                 slug = str(uuid.uuid4())[:10],
                 department_id= dept,
                 desc = desc,
                 item_pen_no=item_pen_no,
                 item_book_no=item_book_no,
                 item_paper_no=item_paper_no,
            )
        purpose.save()
        return render(request,"success.html",{'purpose':purpose})
def breturn(request,slug="return"):
     if request.method == "GET":
         context={
             'department':Department.objects.all()
         }
         return render(request ,"return.html",context)
     elif request.method == "POST":
        title = request.POST.get('title')
        dept = request.POST.get('department')
        bookname = request.POST.get('bookname')
        author = request.POST.get('author')
        bookdate  = request.POST.get('bookdate')
        comments= request.POST.get('comments')
        purpose = Purpose(
             user = request.user ,
             slug=str(uuid.uuid4())[:10],
             name=title,
             department_id=dept,
             booktitle = bookname,
             bookauthor = author,
             checkedin = bookdate,
             desc=comments,
        )
        purpose.save()
        return render(request,"success.html",{'purpose':purpose})






