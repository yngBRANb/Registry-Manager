from django.contrib import admin
from django.urls import path, include
from web.views import *
from django.contrib.auth import views as auth_views
from . import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('errorpage/<int:id>', errorPage, name='errorPage'),
    path('search/', search, name="search"),
    path('category/<int:id>', category_page, name='category'),
    path("ckeditor5/", include('django_ckeditor_5.urls'), name="ck_editor_5_upload_file"),
]


urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
