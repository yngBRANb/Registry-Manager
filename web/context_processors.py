from .models import *

def categories(request):
    categories = Category.objects.all()
    return {"categories": categories}