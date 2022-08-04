from django.views.generic import ListView, UpdateView, CreateView, DetailView, DeleteView  # импортируем класс получения деталей объекта
from django.views.generic.edit import CreateView
from .models import Post, Category, BaseRegisterForm, Author
# from datetime import datetime, date, timedelta
# from django.core.paginator import Paginator
# from .filters import PostFilter
from .forms import CategoryForm, PostForm #,UserForm,
from django.contrib.auth.models import User#, Group
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.views.generic import TemplateView
# from django.shortcuts import redirect,render
# from django.contrib.auth.decorators import login_required
# from django.core.mail import send_mail
from django.http import HttpResponseRedirect
# from .tasks import hello, printer, new_news, send_news_update
# from django.http import HttpResponse
# from django.views import View
# from django.db.models.signals import post_save,m2m_changed
# from django.core.cache import cache


class CategoryList(ListView):
    model = Category
    template_name = 'category.html'
    context_object_name = 'category'
    queryset = Category.objects.order_by('-id')
#    paginate_by = 10
    form_class = CategoryForm
class BaseRegisterView(CreateView):
    model = User
    form_class = BaseRegisterForm
    success_url = '/'
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data.get("first_name")
            last_name = form.cleaned_data.get("last_name")
            email = form.cleaned_data.get("email")
            subject = f' Hello, {first_name}   {last_name}'
            form.save()
            print(subject)

#        send_mail(
#            subject=subject,
#            message='Спасибо за регистрацию на сайте NewsPortal',
#            from_email='VA9979549@yandex.ru',
#            recipient_list=[email]
#        )

        return HttpResponseRedirect('/posts/')

class UserDetailView(LoginRequiredMixin, TemplateView):
    template_name = 'user_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_not_authors'] = not self.request.user.groups.filter(name='authors').exists()
        return context

class PostsList(ListView):
     model = Post
     template_name = 'posts.html'
     context_object_name = 'posts'
     queryset = Post.objects.order_by('-id')
     paginate_by = 12
     form_class = PostForm

#
#
#     # метод get_context_data нужен нам для того, чтобы мы могли передать переменные в шаблон. В возвращаемом словаре context будут храниться все переменные. Ключи этого словаря и есть переменные, к которым мы сможем потом обратиться через шаблон
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['time_now'] = datetime.now()  # добавим переменную текущей даты time_now
#         context['filter'] = PostFilter(self.request.GET, queryset=self.get_queryset())  # вписываем наш фильтр в контекст
#         return context
#
#     def post(self, request, *args, **kwargs):
#         form = self.form_class(request.POST)  # создаём новую форму, забиваем в неё данные из POST-запроса
#
#         if form.is_valid():  # если пользователь ввёл всё правильно и нигде не ошибся, то сохраняем новый товар
#             form.save()
#
#         return super().get(request, *args, **kwargs)
#
#  # создаём представление, в котором будут детали конкретного отдельного товара
class PostDetail(DetailView):
     model = Post  # модель всё та же, но мы хотим получать детали конкретно отдельного товара
     template_name = 'post_detail.html'  # название шаблона будет product.html
     context_object_name = 'postdetail'  # название объекта. в нём будет




class PostCreateView(PermissionRequiredMixin, CreateView):
     permission_required = ('main.add_post',)
     template_name = 'posts_create.html'
     form_class = PostForm

#     def post(self, request, *args, **kwargs):
#        # post = Post(
#        #     id_author=Author.objects.get(id_user=request.user),
#        #     header=request.POST['header'],
#        #     text=request.POST['text']
#        #)
#        #post.save()
#          post = Post(
#              id_author=Author.objects.get(User=request.user),
#              heder=request.POST['heder'],
#              text=request.POST['text']
#             )
# #         print(post.text + 'dfsdfsdf' + post.heder + str(post.time_in))
# #         print ('author_id'+ str(post.author_id))
#          post.save()
# #         #print('def post')
# #         #print(post.header)
# #
# #
class PostUpdateView(UpdateView):
    template_name = 'news_create.html'
    form_class = PostForm

     # метод get_object мы используем вместо queryset, чтобы получить информацию об объекте, который мы собираемся редактировать
    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Post.objects.get(pk=id)
#
#
# дженерик для удаления товара
class PostDeleteView(DeleteView):
    template_name = 'posts_delete.html'
    queryset = Post.objects.all()
    success_url = '/posts/'
# # Create your views here.
