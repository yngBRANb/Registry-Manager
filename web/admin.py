from django.contrib import admin
from .models import Error, Category, TelegramUser

@admin.register(Error)
class ErrorAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'status', 'decision')
    list_filter = ('category', 'status', 'decision')
    search_fields = ('name', 'description')

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(TelegramUser)
class TelegramUserAdmin(admin.ModelAdmin):
    list_display = ('chat_id',)
    search_fields = ('chat_id',)
