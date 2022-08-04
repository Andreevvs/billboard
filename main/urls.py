from django.urls import path
#from .views import NewsList, NewsDetail, NewsSearch, PostCreateView,PostUpdateView, PostDeleteView, UserDetailView, BaseRegisterView, upgrade_me, add_subscribe, del_subscribe
from .views import BaseRegisterView
from .views import CategoryList ,BaseRegisterView,PostsList, PostCreateView,PostDetail, PostUpdateView, PostDeleteView, UserDetailView
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
    path('', PostsList.as_view()),
    path('<int:pk>', PostDetail.as_view(), name='posts_detail'),
    path('add/', PostCreateView.as_view(), name='posts_create'),
    path('<int:pk>/edit', PostUpdateView.as_view(), name='posts_update'),
    path('<int:pk>/delete', PostDeleteView.as_view(), name='posts_delete'),
    path('user/', UserDetailView.as_view(), name='user_detail'),
    path('logout/', LogoutView.as_view(template_name = 'logout.html'), name='logout'),
    path('login/', LoginView.as_view(template_name='login.html'),name='login'),
    path('signup/', BaseRegisterView.as_view(template_name = 'signup.html'), name='signup'),
    # path('upgrade/', upgrade_me, name='upgrade'),
    path('category/', CategoryList.as_view()),
    path('signup/', BaseRegisterView.as_view(template_name='signup.html'), name='signup'),
    ]