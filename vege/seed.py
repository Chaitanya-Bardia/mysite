from faker import Faker
import random
from .models import *
from django.db.models import Sum
from vege import *
fake = Faker()

def createsubmarks(n):
    try:
        student_obj = Student.objects.all()
        for student in student_obj:
            subjects = Subject.objects.all()
            for subject in subjects:
                Subjectmarks.objects.create(
                    subject = subject,
                    student = student,
                    marks = random.randint(0,100)
                )
    except Exception as e:
        print(e)

arr = []
def seed_db(n=100) -> None:
    try:
        for i in range(0,n):
            no = random.randint(1,100)
            if no in arr:
                continue
            else:
                arr.append(no)
            dept_obj = Department.objects.all()
            rand_index = random.randint(0,len(dept_obj)-1)
            department = dept_obj[rand_index]
            studentid = f'H0{no}'
            sname = fake.name()
            semail = fake.email()
            sage = random.randint(20,30)
            saddress = fake.address()

            stuid_obj = Studentid.objects.create(studentid = studentid)
            student_obj = Student.objects.create(
                department = department,
                studentid = stuid_obj,
                sname = sname,
                semail = semail,
                sage = sage,
                saddress = saddress,
            )
    except Exception as e:
        print (e)

def generate_marksheet():
    current_rank = -1
    ranks = Student.objects.annotate(marks = Sum('studentmarks__marks')).order_by('-marks','-sage')
    i = 1
    for rank in ranks:
        reportcard.objects.create(
            student = rank,
            student_rank = i,
        )
        i += 1