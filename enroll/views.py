from django.shortcuts import render, HttpResponseRedirect
from . form import UserRegistration
from . models import User
# Create your views here.

def add_show(request):
    if request.method == 'POST':
        fm = UserRegistration(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            pw = fm.cleaned_data['password']
            reg = User(name=nm, email=em, password=pw)
            reg.save()
            fm = UserRegistration()
    else:
        fm = UserRegistration()
    userde = User.objects.all()
    return render(request, 'enroll/addandshow.html', {'form':fm, 'user':userde})

def updateData(request, id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        fm = UserRegistration(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi = User.objects.get(pk=id)
        fm = UserRegistration(instance=pi)
    return render(request, 'enroll/updatestudent.html', {'form':fm})

def deleteData(request, id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')