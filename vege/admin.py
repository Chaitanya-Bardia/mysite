from django.contrib import admin
from .models import *
from django.db.models import Sum
# Register your models here.
admin.site.register(recipe)
admin.site.register(Department)
admin.site.register(Studentid)
admin.site.register(Student)
admin.site.register(Subject)
class submarksadmin(admin.ModelAdmin):
    list_display = ['student','subject','marks']

admin.site.register(Subjectmarks,submarksadmin)

class reportcardAdmin(admin.ModelAdmin):
    list_display = ['student','student_rank','total_marks','date_of_marksheet_generation']
    ordering = ['student_rank']
    def total_marks(self,obj):
        subject_marks = Subjectmarks.objects.filter(student = obj.student)
        marks = (subject_marks.aggregate(marks = Sum('marks')))
        return marks['marks']
admin.site.register(reportcard,reportcardAdmin)