from django.shortcuts import render, HttpResponse,redirect
from .models import User

# Create your views here.
def allusers(request):
    context = {
        "allusers": User.objects.all() 
    }

    return render(request, "index.html", context=context)

def userform(request):
    return render(request, "adduser.html")

def adduser(request):
    if request.method == 'POST':
        User.objects.create(full_name=request.POST['fullname'], email=request.POST['email'])
    
    return redirect('/')

def showuser(request,id):
    context = {
        "user" : User.objects.get(id=id)
    }

    return render(request, "showuser.html", context=context)

def edituser(request,id):
    context = {
        "user_id" : id
    }

    return render(request, "edituser.html", context=context)

def updateuser(request,id):
    if request.method == 'POST':
        user = User.objects.get(id=id)

        user.full_name = request.POST['fullname']
        user.email = request.POST['email']

        user.save()
    
    return redirect('/')

def deleteuser(request,id):
   user = User.objects.get(id=id)

   user.delete() 

   return redirect('/')