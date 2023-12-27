from django.shortcuts import render,HttpResponse,redirect
from .models import User, Post

# Create your views here.
def index(request):
    errors = []
    if 'errors' in request.session and len(request.session['errors']) > 0:
        errors = request.session['errors']
        del request.session['errors']

    context = {
        "errors": errors
    }

    return render(request,"index.html", context = context)

def register(request):
    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        password = request.POST['password']

        request.session['errors'] = []

        if len(fname) < 2:
            request.session['errors'].append("First name must be at least 2 characters")
        if len(lname) < 2:
            request.session['errors'].append("Last name must be at least 2 characters")

        if len(request.session['errors']) > 0:
            return redirect('/')
        
        user = User.objects.create(first_name = fname, last_name = lname, email = email, password = password)

        request.session['user_id'] = user.id

        return redirect('/newsfeed')
    else:
        return redirect('/')

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = User.objects.filter(email = email, password = password).first()

        if not user:
           request.session['errors'] = []
           request.session['errors'].append('Invalid Email/password combination')

           return redirect('/')
        
        request.session['user_id'] = user.id

        return redirect('/newsfeed')
    else:
        return redirect('/')

def newsfeed(request):
   if 'user_id' in request.session: 
    user = User.objects.get(id = request.session['user_id'])
    
    context = {
        "posts": Post.objects.all(),
        "username": user.first_name
    } 
    
    return render(request, 'newsfeed.html', context = context)
   else:
       return redirect('/')
   
def addpost(request):
    if request.method == 'POST':
        post = Post.objects.create(name = request.POST['name'], post = request.POST['post'])
        return redirect('/newsfeed')

def logout(request):
    del request.session['user_id']

    return redirect('/')