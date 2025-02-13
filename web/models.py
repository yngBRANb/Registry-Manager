from django.db import models
from django.contrib.auth.models import User

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

    def __str__ (self):
        return self.name

class Error(models.Model):
    name = models.CharField(verbose_name="Название ошибки", max_length=50)
    description = models.TextField(verbose_name="Описание ошибки")
    solving = models.TextField(verbose_name="Решение ошибки")
    created_date = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=CLASSIFICATION, default='no')
    decision = models.CharField(max_length=30, choices=DECISION, default='no')
    photo = models.ImageField(null=True ,upload_to='errors/%Y-%m-%d/')
    category = models.ForeignKey(Category , on_delete=models.CASCADE, verbose_name="Категория")

    def __str__(self):
        return self.name
