from django.db import models
from django.contrib.auth.models import User
from django_ckeditor_5.fields import CKEditor5Field


CLASSIFICATION = (
    ('Red', 'Красная'),
    ('Yellow', 'Желтая'),
    ('Green', 'Зелёная'),
    ('no', 'no'),
)

DECISION = (
    ('Red', 'Сложно'),
    ('Yellow', 'Среднее'),
    ('Green', 'Легко'),
    ('no', 'no'),
)

class Category(models.Model):
    name = models.CharField(verbose_name="Категории", max_length=50)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__ (self):
        return self.name

class Error(models.Model):
    name = models.CharField(verbose_name="Название ошибки", max_length=50,)
    description = CKEditor5Field(verbose_name="Описание ошибки")
    solving = CKEditor5Field(verbose_name="Решение ошибки")
    created_date = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=CLASSIFICATION, default='no', verbose_name="Статус ошибки")
    decision = models.CharField(max_length=30, choices=DECISION, default='no', verbose_name="Сложность решения")
    photo = models.ImageField(null=True ,upload_to='errors/%Y-%m-%d/', verbose_name="Фото ошибки")
    category = models.ForeignKey(Category , on_delete=models.CASCADE, verbose_name="Категория")

    class Meta:
        verbose_name = 'Записи ошибок'
        verbose_name_plural = 'Записи ошибок'    

    def __str__(self):
        return self.name

class TelegramUser(models.Model):
    chat_id = models.CharField(max_length=20, unique=True, verbose_name="Chat ID")
    
    class Meta:
        verbose_name = "Пользователь Telegram"
        verbose_name_plural = "Пользователи Telegram"
    
    def __str__(self):
        return self.chat_id
