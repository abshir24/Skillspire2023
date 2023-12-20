from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
    if 'counter' not in request.session:
        request.session['counter'] = 0
    else:
        request.session['counter'] += 1
    return HttpResponse(request.session['counter'])

def addtwo(request):
    if request.session['counter'] == None:
        request.session['counter'] = 2
    else:
        request.session['counter'] += 2
    return HttpResponse(request.session['counter'])

def reset(request):
    del request.session['counter']

    return redirect('/')
