from django.shortcuts import render,HttpResponse
from datetime import datetime
import pytz

# Create your views here.

def index(request):
    # seattleTz = pytz.timezone("America/Los_Angeles") 
    context = {
        "time": datetime.now()
    }
    return render(request,"index.html", context = context)