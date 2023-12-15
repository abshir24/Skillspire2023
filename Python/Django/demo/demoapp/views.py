from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,"home.html")

def coding(request):
    context = {
        "playlist": [{"No":1, "Track":"testcodingtrack", "Artist": "testcodingartist", "Length":"testcodinglength"}]
    }
    return render(request,"coding.html", context=context)

def earth(request):
    return render(request,"earth.html")
