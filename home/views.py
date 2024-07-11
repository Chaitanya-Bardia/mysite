from django.shortcuts import render,redirect
import random
from django.http import HttpResponse
from .utils import send_email_to_client,send_email_with_attachment
from django.conf import settings
from home.models import *
# Create your views here.

def send_email(req):
    subject = "This E-mail is from Django server with attachments"
    message = "Please refer  the attached file"
    file_path = f"{settings.BASE_DIR}/public/static/recipe1.jpg"
    recipient_list = ["chaitanyabardia@gmail.com"]
    send_email_with_attachment(subject,message,file_path,recipient_list)
    return redirect('/')

def home(req):
    car.objects.create(cname = f"Nexon-{random.randint(0,100)}",speed = 100)
    people = [{'Name':'Chaitanya','Age':19},{'Name':'Adarsh','Age':17},{'Name':'Mithles','Age':18},{'Name':'Kartik','Age':15}]
    return render(req,"index.html",context={'page': 'Index Page','peoples':people})
def contact(req):
    context = {'page':'contact'}
    return render(req,"contact.html",context)
def about(req):
    context = {'page':'about'}
    return render(req,"about.html",context)
def successpg(req):
    print("*" * 5)
    return HttpResponse("<h2> Hello,This is a success page</h2>")
    
