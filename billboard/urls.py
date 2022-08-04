from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView
from main.views import UserDetailView
from django.contrib.sites.models import Site

urlpatterns = [
    path('admin/', admin.site.urls),
    path('posts/', include('main.urls')),  # делаем так, чтобы все адреса из нашего приложения (simpleapp/urls.py) сами автоматически подключ
   # path('accounts/', include('allauth.urls')),
    #path('', UserDetailView.as_view()),
    #path('account/', include('account.urls')),
   ]
