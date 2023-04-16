from django.shortcuts import render, HttpResponse
from home.models import Visitor, Prisoner, Guard
from django.contrib import messages

# Create your views here.
def index(request):
    context = {
        'variable':"this is sent"
    }
    return render(request, 'index.html', context)
    #return HttpResponse("this is homepage")

def prisoner(request):
    if request.method == "POST":
        pid = request.POST.get('id')
        name = request.POST.get('name')
        edate = request.POST.get('edate')
        rdate = request.POST.get('rdate')
        seclvl = request.POST.get('seclvl')
        cell = request.POST.get('cellsharing')
        cdate = request.POST.get('curdate')
        prisoner = Prisoner(pid=pid, name=name, EnteranceDate=edate, ReleaseDate=rdate, SecurityLevel=seclvl, cellSharing=cell, CurrentDate=cdate)
        prisoner.save()
        messages.success(request, "Prisoner record added")

    
    return render(request, 'prisoner.html')
   

    

def visitor(request):
    if request.method == "POST":
        vid = request.POST.get('id')
        name = request.POST.get('name')
        gender = request.POST.get('gender')
        address = request.POST.get('address')
        visitor = Visitor(vid=vid, name=name, gender=gender, address=address)
        visitor.save()
        messages.success(request, "Visitor record added")

    return render(request, 'visitor.html')
    
def guard(request):
    if request.method == "POST":
        gid = request.POST.get('id')
        name = request.POST.get('name')
        password = request.POST.get('password')
        address = request.POST.get('address')
        shift = request.POST.get('shift')
        guard = Guard(Gid=gid, name=name, password=password, address=address, shift=shift)
        guard.save()
        messages.success(request, "Guard record added")

    return render(request, 'guard.html')

