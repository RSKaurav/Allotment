from django.shortcuts import render,render_to_response,redirect
from django.http import  HttpResponse, HttpResponseRedirect
from django.conf import settings
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Student,Room
# Create your views here.

def  index(request):
	return render(request,'index.html')

def Registration(request):
    return render(request,'Student_Registration.html')

def Rooms(request):
    return render(request,'Rooms.html')

def saveData(request):
    if request.method == 'POST':
        tzid = request.POST["tzid"]
        sname = request.POST['sname']
        gen = request.POST['opt']
        con = request.POST['con']
        email = request.POST['email']
        ins = request.POST['ins']
        add = request.POST['add']
        obj = Student()
        obj.tzid = tzid
        obj.sname = sname
        obj.gender = gen
        obj.contact = con
        obj.email = email
        obj.institute = ins
        obj.address = add
        obj.save()
    return redirect('/Hostel_mgmnt/index')

def Room_Save(request):
    if request.method == 'POST':
        hst = request.POST["hst"]
        blck = request.POST['blck']
        floorno = request.POST['floorno']
        roomno = request.POST['roomno']
        cpc = request.POST['cpc']
        obj = Room()
        a,b=blck.split(',')
        obj.roomNo = hst+"_"+b+"_"+floorno+"_"+roomno
        obj.floorNo = floorno
        obj.blkid = int(a)
        obj.capacity = cpc
        obj.availability = cpc
        obj.save() 
    return redirect('/Hostel_mgmnt/index')

def EmptyRoom(request):
	roomsobj=Room.objects.all()
	return render(request,'EmptyRoom.html',{'Data':roomsobj,})

def EnterTzId(request):
	print (request.GET.get('roomNo'))
	return render(request,'EnterTzId.html',{'roomNo': request.GET.get('roomNo'),})
