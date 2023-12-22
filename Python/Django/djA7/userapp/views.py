from django.shortcuts import render, HttpResponse,redirect
from .models import User

# Create your views here.

def index(request):
    context = {
        'allusers' : User.objects.all()
    }
    return render(request,"index.html", context = context)

def adduser(request):
    if request.method == 'POST':
        User.objects.create(name = request.POST['name'], 
                            height = request.POST['height'], 
                                weight = request.POST['weight'], 
                                    diet= request.POST['diet'])
    
    return redirect('/')

def displayuser(request,id):
   context = {
       'user' : User.objects.get(id=id) 
   }

   return render(request, 'userinfo.html', context=context)

