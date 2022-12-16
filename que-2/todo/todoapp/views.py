from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
# Create your views here.

def index(request):
    data=TodoTask.objects.all()
    return render(request, 'home.html',{'data':data})

def add(request):
    if request.method == 'GET':
        tas=request.GET['task']
        obj=TodoTask()
        obj.task=tas
        obj.save()
    return render(request, 'add.html')

def delete(request,id):
    data=TodoTask.objects.get(id=id)
    data.delete()
    return render(request,'home.html')

def update(request,id):
    data=TodoTask.objects.filter(id=id)
    data.update(task="Hello")
    data=TodoTask.objects.all()
    return render(request,'home.html',{'data':data})


