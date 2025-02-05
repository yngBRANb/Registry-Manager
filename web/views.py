from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from .models import *
from django.contrib.auth.decorators import login_required

def login_view(request):
    return render(request, 'login.html')  # Render the login form if GET request

def index(request):
    error = Error.objects.all()
    return render(request, 'index.html', { "errors" : error })

@login_required
def errorPage(request, id):
    error = Error.objects.get(id=id)
    return render(request, 'error.html', { "errors" : error })

@login_required
def search(request):
    request.method=="GET"
    select = request.GET['select']
    searchq = request.GET['search']
    
    if select == "id":
        errors = Error.objects.filter(id__contains=request.GET['search'])
    elif select == "name":
        errors=Error.objects.filter(name__contains=searchq)
    else:
        errors=Error.objects.filter(name__contains=searchq)
        
    return render(request, 'search.html', { "errors" : errors })