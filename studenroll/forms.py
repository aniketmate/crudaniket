from django import forms
from django.forms import fields, widgets
from .models import Student_Profile

class StudentRegistration(forms.ModelForm):
    class Meta:
        model = Student_Profile
        fields = ['name','email','password']
        widgets = {
            'name' : forms.TextInput(attrs={'class':'form-control'}),
            'email' : forms.EmailInput(attrs={'class':'form-control'}),
            'password' : forms.PasswordInput(render_value=True, attrs={'class':'form-control'})

        }