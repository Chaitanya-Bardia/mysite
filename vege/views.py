from django.shortcuts import render,redirect
from .models import *
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q,Sum
from .seed import generate_marksheet
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your views here.
@login_required(login_url="/login/")
def recipes(req):
    if req.method == "POST":
        data = req.POST
        rimage = req.FILES.get('rimage')
        rname = data.get('rname')
        rdescription = data.get('rdescription')

        recipe.objects.create(
            rname = rname,
            rdescription = rdescription,
            rimage = rimage,
        )
        return redirect('/recipes/')    
    queryset = recipe.objects.all()

    if req.GET.get('search'):
        queryset= queryset.filter(rname__icontains = req.GET.get('search'))
    context = {'recipes':queryset}
    return render(req,'recipes.html',context)

def updaterecipe(req,slug):
    queryset = recipe.objects.get(slug = slug)
    if req.method == "POST":
        data = req.POST
        rimage = req.FILES.get('rimage')
        rname = data.get('rname')
        rdescription = data.get('rdescription')
        queryset.rname = rname
        queryset.rdescription = rdescription
        if rimage:
            queryset.rimage = rimage
        queryset.save()
        return redirect('/recipes/')
    
    context = {'recipes':queryset}
    return render(req,'updaterecipes.html',context)

def deleterecipe(req,id):
    queryset = recipe.objects.get(id = id)
    queryset.delete()
    return redirect('/recipes/')

def loginpg(req):
    if req.method == "POST":
        username = req.POST.get('username')
        password = req.POST.get('password')

        if not User.objects.filter(username = username).exists():
            messages.error(req, "Usernname doesn't exist")
            return redirect('/login/')
        
        user = authenticate(username = username, password = password)

        if user is None:
            messages.error(req, "Incorrect Password")
            return redirect('/login/')
        
        else:
            login(req,user)
            return redirect('/recipes/')

    return render(req,'login.html')

def logoutpg(req):
    logout(req)
    return redirect('/login/')

def register(req):
    if req.method == "POST":
        first_name = req.POST.get('first_name')
        last_name = req.POST.get('last_name')
        username = req.POST.get('username')
        password = req.POST.get('password')

        user = User.objects.filter(username = username)
        if user.exists():
            messages.info(req, "Username already exists.")
            return redirect('/register/')

        user = User.objects.create(
            first_name = first_name,
            last_name = last_name,
            username = username,
        )
        user.set_password(password)
        user.save()
        messages.info(req, "Account Created Successfully.")
        return redirect('/register/')
    
    return render(req,'register.html')

def get_student(req):
    queryset = Student.objects.all()

    if req.GET.get('search'):
        search = req.GET.get('search')
        queryset = queryset.filter(
            Q(sname__icontains = search) |
            Q(department__department__icontains = search) |
            Q(studentid__studentid__icontains = search) |
            Q(sage__icontains = search)
            )
    paginator = Paginator(queryset, 10)
    page_number = req.GET.get("page",1)
    page_obj = paginator.get_page(page_number)
    return render(req,'students.html',{'queryset':page_obj})

def seemarks(req,studentid):
    queryset = Subjectmarks.objects.filter(student__studentid__studentid = studentid)
    totalmarks = queryset.aggregate(totalmarks = Sum('marks'))
    return render(req,'see_marks.html',{'queryset':queryset,'totalmarks':totalmarks})
