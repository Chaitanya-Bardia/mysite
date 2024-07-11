from home.models import student
import time
from django.core.mail import send_mail,EmailMessage
from django.conf import settings


def send_email_to_client():
    subject = "This email is from Django server"
    message = "This is a test message from Django server"
    from_email = settings.EMAIL_HOST_USER
    recipient_list = ["chaitanyabardia@gmail.com"]

    send_mail(subject,message,from_email,recipient_list)

def send_email_with_attachment(subject,message,file_path,recipient_list):
    mail = EmailMessage(subject=subject,body = message,from_email=settings.EMAIL_HOST_USER, to = recipient_list)
    mail.attach_file(file_path)
    mail.send()