from django.shortcuts import render
from.models import login,registration,addbook
from django.http import HttpResponse
# Create your views here.
def display(request):
    return render(request,'login.html')
def display1(request):
    if request.method=="POST":
        a=request.POST['a1']
        b=request.POST['a2']
        data=login.objects.create(username=a,password=b)
        data.save()
        if data.password==b:
            return render(request,"dashboard.html")
        else:
            return HttpResponse('username and passord is incorrect')
    else:
        return render(request,'login.html')
def display2(request):
    return render(request,'register.html')
def display3(request):
    if request.method=='POST':
        a=request.POST['b1']
        b=request.POST['b2']
        c=request.POST['b3']
        d=request.POST['b4']
        data=registration.objects.create(name=a,age=b,username=c,password=d)
        data.save()
        return render(request,'login.html')
def display4(request):
    return render(request,'addbook.html')
def display5(request):
    if request.method=="POST":
        a=request.POST['c1']
        b=request.POST['c2']
        c=request.POST['c3']
        d=request.POST['c4']
        data=addbook.objects.create(bookid=a,bookname=b,bookauthur=c,bookprice=d)
        data.save()
        return render(request,'dashboard.html')
def display7(request):
    if request.method=="GET":
        data=addbook.objects.all()
        return render(request,'display.html',{'y':data})

def display8(request):
    return render(request,'dashboard.html')
def display9(request):
    return render(request,'search.html')
def display10(request):
    if request.method=="POST":
        a=request.POST['d1']
        data=addbook.objects.filter(bookid=a)
        return render(request,'search.html',{'y':data})
def display11(request):
    return render(request,'delete.html')



