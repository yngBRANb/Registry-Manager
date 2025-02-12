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
    errors = Error.objects.filter(name__contains=request.GET['search'])
        
    return render(request, 'search.html', { "errors" : errors })

@login_required
def category_page(request, id):
    category = Error.objects.filter(category=id)

    return render(request, 'category.html', { "category" : category })