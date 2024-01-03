from django.shortcuts import render, HttpResponse,redirect

# Create your views here.
def index(request):
    context = {
        "data": "INDEX"
    }

    return render(request, "index.html", context=context)

def userdata(request):
    if request.method == 'POST':
        context = {
            'name' : request.POST['name'],
            'vacation' : request.POST['vacation'],
            'food': request.POST['food']
        }

        return render(request, "data.html", context=context)
    
    return redirect('/')
