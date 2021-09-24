from django.contrib import admin
from .models import Student_Profile
# Register your models here.
@admin .register(Student_Profile)
class Student_Profile_Admin(admin.ModelAdmin):
    list_display = ('id','name','email','password')
