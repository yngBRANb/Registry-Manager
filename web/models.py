from django.db import models

CLASSIFICATION = (
    ('Red', 'Красная'),
    ('Yellow', 'Желтая'),
    ('Green', 'Зелёная'),
    ('no', 'no'),
)

class Error(models.Model):
    name = models.CharField(verbose_name="Название ошибки", max_length=50)
    description = models.TextField(verbose_name="Описание ошибки")
    solving = models.TextField(verbose_name="Решение ошибки")
    created_date = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=CLASSIFICATION, default='no')
    photo = models.ImageField(null=True ,upload_to='errors/%Y-%m-%d/')
    
    def __str__(self):
        return self.name
    