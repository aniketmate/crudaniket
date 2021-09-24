from django.shortcuts import render,HttpResponseRedirect
from .forms import StudentRegistration
from .models import Student_Profile

# Create your views here.
def add_and_show(request):
    """Function will add and show"""
    if request.method == 'POST':
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            pw = fm.cleaned_data['password']
            reg = Student_Profile(name=nm,email=em,password=pw)
            reg.save()
            # fm.save()
            fm = StudentRegistration()
    else:
        fm = StudentRegistration()
    stud = Student_Profile.objects.all()
    return render(request, 'studenroll/addandshow.html',{'form': fm,'stud':stud})

def delete(request,id):
    """This function will delete"""
    if request.method == "POST":
        pi = Student_Profile.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')

def update(request,id):
    """This function will update"""
    if request.method == 'POST':
        pi = Student_Profile.objects.get(pk=id)
        fm = StudentRegistration(request.POST,instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi = Student_Profile.objects.get(pk=id)
        fm = StudentRegistration(instance=pi)
    return render(request, 'studenroll/updatestud.html',{'form': fm})