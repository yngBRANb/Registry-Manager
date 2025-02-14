from django.shortcuts import render
from django.core.paginator import Paginator
from django.core.paginator import Paginator
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from .models import *
from django.contrib.auth.decorators import login_required

def login_view(request):
    return render(request, 'login.html')  # Render the login form if GET request

def index(request):
    errors_list = Error.objects.all()
    paginator = Paginator(errors_list, 9)  # 9 ошибок на страницу
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'index.html', {'page_obj': page_obj})

@login_required
def errorPage(request, id):
    error = Error.objects.get(id=id)
    return render(request,'error.html', { "errors" : error })

@login_required
def search(request):
    request.method=="GET"
    errors = Error.objects.filter(name__contains=request.GET['search'])
        
    return render(request, 'search.html', { "errors" : errors })

@login_required
def category_page(request, id):
    category = Error.objects.filter(category=id)
    
    return render(request, 'category.html', { "category" : category })
