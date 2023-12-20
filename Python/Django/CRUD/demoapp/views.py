from django.shortcuts import render, HttpResponse,redirect
from .models import Post

# Create your views here.
def home(request):
    context = {
        "allposts": Post.objects.all()
    }
    return render(request, 'post.html', context = context)

def addpost(request):
    if request.method == 'POST':
       Post.objects.create(post = request.POST['post'])  

    return redirect('/')

def edit(request,id):
    if request.method == 'POST':
        post = Post.objects.get(id=id)
        post.post = request.POST['post']
        post.save()
        return redirect('/')
    else:
        context = {
            'post' : Post.objects.get(id=id)
        }
        return render(request,'edit.html', context = context)

def delete(request,id):
    post = Post.objects.get(id=id)

    post.delete()

    return redirect('/')