from django.shortcuts import render, HttpResponse,redirect
from .models import User

# Create your views here.
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        user = User.objects.create(username=username, email = email, password = password)

        return render(request,"formdata.html",context = { "user" : user})
    else:
        return redirect('/')

def update(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        
        user = User.objects.filter(email = email).first()

        if user:
            user.username = username
            user.save()
            return render(request,"formdata.html",context = { "user" : user})
        else:
            return HttpResponse('User does not exist')
    return redirect('/')

def home(request):
    return render(request,"index.html")

def coding(request):
    context = {
        "playlist": [{"No":1, "Track":"testcodingtrack", "Artist": "testcodingartist", "Length":"testcodinglength"}]
    }
    return render(request,"coding.html", context=context)

def earth(request):
    return render(request,"earth.html")
