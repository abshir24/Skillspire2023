from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    context = {
        "data": "INDEX"
    }

    return render(request, "index.html", context=context)

def displayname(request):
    context = {
        "data":"name",
        "name": "Abshir"
    }

    return render(request, "index.html", context=context)

def displayfood(request):
    context = {
        "data":"food",
        "food": "Salad"
    }

    return render(request, "index.html", context=context)

def displayvacation(request):
    context = {
        "data": "vacation",
        "vacation": "Barbados"
    }

    return render(request, "index.html", context=context)
