from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms

# Create your models here.
class Post(models.Model):
    author = models.ForeignKey("Author", on_delete=models.CASCADE)
    time_in = models.DateTimeField(auto_now_add=True)
    header = models.CharField(max_length=128, default="")
    text = models.TextField(null = True)
    category = models.ForeignKey("Category", on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.header.title()}'

    def get_absolute_url(self):  # добавим абсолютный путь, чтобы после создания нас перебрасывало на страницу с товаром
        return f'/posts/{self.id}'

    # def save(self, *args, **kwargs):
    #     super().save(*args, **kwargs)  # сначала вызываем метод родителя, чтобы объект сохранился
    #     cache.delete(f'post-{self.pk}')  # затем удаляем его из кэша, чтобы сбросить его

class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rate = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.user.username.title()}'


class Category(models.Model):
    category = models.CharField(max_length=64, unique=True)

    def __str__(self):
        return f'{self.category.title()}'

class Response(models.Model):
    author = models.ForeignKey("Author", on_delete=models.CASCADE)
    time_in = models.DateTimeField(auto_now_add=True)
    text = models.TextField(null = True)

    def __str__(self):
        return f'{self.text.title()}'

class BaseRegisterForm(UserCreationForm):
    email = forms.EmailField(label = "Email")
    first_name = forms.CharField(label = "Имя")
    last_name = forms.CharField(label = "Фамилия")

    class Meta:
        model = User
        fields = ("username",
                  "first_name",
                  "last_name",
                  "email",
                  "password1",
                  "password2", )