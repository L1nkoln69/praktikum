from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse
from django.views.generic import ListView, TemplateView, DetailView, CreateView, FormView, UpdateView
from .models import Post
from django.contrib.auth import logout
from django.core.mail import send_mail
from .forms import PostForm, ToAdminForm, RegistrUserForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin


def sample_view(request):
    html = '<body><h1>Django sample_view</h1><br><p>Отладка sample_view</p></body>'
    return HttpResponse(html)


class AllPosts(ListView):
    model = Post
    template_name = 'posts.html'
    context_object_name = 'post_list'
    paginate_by = 5


class Home(TemplateView):
    template_name = 'home_page.html'


class PostDetail(DetailView):
    model = Post
    template_name = 'one_post.html'
    pk_url_kwarg = 'pk'
    context_object_name = 'post'


class CreatePost(CreateView):
    form_class = PostForm
    template_name = 'post_form.html'
    success_url = reverse_lazy('home_page')
    success_message = 'Post successfully created'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class MessageAdmin(SuccessMessageMixin, FormView):
    template_name = 'message_admin.html'
    form_class = ToAdminForm
    success_url = reverse_lazy('home_page')
    success_message = 'Your message has been sent'

    def form_valid(self, form):
        send_mail('MESSAGE',
                  f'Ok',
                  'orlov229003@gmail.com',
                  ['orlav228007@gmail.com'],
                  fail_silently=False
                  )
        return super().form_valid(form)


class RegistrationUser(CreateView):
    form_class = RegistrUserForm
    template_name = 'registration.html'
    success_url = reverse_lazy('posts')

    def form_valid(self, form):
        user = form.save()
        user = authenticate(username=user.username, password=user._password)
        login(self.request, user)
        return super().form_valid(form)


class LoginUser(LoginView):
    form_class = AuthenticationForm
    template_name = 'login.html'

    def get_success_url(self):
        return reverse_lazy('home_page')


def logout_user(request):
    logout(request)
    return redirect('home_page')


class UpdateProfile(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = User
    fields = ["username", "email"]
    template_name = 'update_user.html'
    success_url = reverse_lazy('home_page')
    success_message = "Profile updated"

    def get_object(self, queryset=None):
        user = self.request.user
        return user


class UserProfile(LoginRequiredMixin, DetailView):
    model = Post
    template_name = 'one_post.html'
    pk_url_kwarg = 'pk'
    context_object_name = 'post'

    def get_object(self, queryset=None):
        user = self.request.user
        return user
