from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from .utils import generate_slug

User = get_user_model()

# Create your models here.

class recipemanager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_deleted = False)
    
class studentmanager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_deleted = False)

class recipe(models.Model):
    user = models.ForeignKey(User, on_delete= models.SET_NULL, null=True , blank = True )
    slug = models.SlugField(unique=True)
    rname = models.CharField(max_length=100)
    rdescription = models.TextField()
    rimage = models.ImageField()
    file = models.FileField()
    rviewcount = models.IntegerField(default=1)
    is_deleted = models.BooleanField(default=False)

    objects = recipemanager()
    admin_objects = models.Manager()

    def save(self,*args,**kwargs):
        self.slug = generate_slug(self.rname)
        super(recipe,self).save(*args,**kwargs)

class Department(models.Model):
    department = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.department
    
    class Meta:
        ordering = ['department']

class Studentid(models.Model):
    studentid = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.studentid
    
class Student(models.Model):
    department = models.ForeignKey(Department,related_name="depart",on_delete=  models.CASCADE)
    studentid = models.OneToOneField(Studentid,related_name="stuid",on_delete=  models.SET_NULL,null = True)
    sname = models.CharField(max_length=100)
    semail = models.EmailField(unique=True)
    sage = models.IntegerField(default=18)
    saddress = models.TextField()
    is_deleted = models.BooleanField(default=False)

    objects = studentmanager()
    admin_objects = models.Manager()


    def __str__(self) -> str:
        return self.sname
    
    class Meta:
        ordering = ['sname','studentid']
        verbose_name = "student"

class Subject(models.Model):
    sname = models.CharField(max_length = 100)

    def __str__(self) -> str:
        return self.sname

class Subjectmarks(models.Model):
    student = models.ForeignKey(Student,related_name ="studentmarks",on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject,on_delete=models.CASCADE)
    marks = models.IntegerField()

    def __str__(self) -> str:
        return f'{self.student.sname}{self.subject.sname}'

    class Meta:
        unique_together = ['student','subject']
    

class reportcard(models.Model):
    student = models.ForeignKey(Student,related_name="studentreportcard",on_delete=models.CASCADE)
    student_rank = models.IntegerField()
    date_of_marksheet_generation = models.DateField(auto_now_add = True)

    class Meta:
        unique_together = ['student_rank','date_of_marksheet_generation']

