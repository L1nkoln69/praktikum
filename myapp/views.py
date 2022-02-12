from django.shortcuts import redirect
# from django.urls import reverse
from django.http import HttpResponseRedirect
from django.views.generic import ListView, TemplateView, DetailView, CreateView, FormView, UpdateView
from .models import Post, Comment
from django.contrib.auth import logout, authenticate, login
from django.core.mail import send_mail
from .forms import ToAdminForm, RegistrUserForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from .forms import CreatePosts

# def sample_view(request):
#     html = '<body><h1>Django sample_view</h1><br><p>Отладка sample_view</p></body>'
#     return HttpResponse(html)


class AllPosts(ListView):
    model = Post
    template_name = 'posts.html'
    context_object_name = 'post_list'
    paginate_by = 5

    def get_queryset(self):
        return Post.objects.filter(is_published=True)


class Home(TemplateView):
    template_name = 'home_page.html'


class MessageAdmin(SuccessMessageMixin, FormView):
    template_name = 'message_admin.html'
    form_class = ToAdminForm
    success_url = reverse_lazy('home_page')
    success_message = 'Your message has been sent'

    def form_valid(self, form):
        data = form.cleaned_data
        send_mail('MESSAGE',
                  data["text"],
                  data['email'],
                  ['orlav228007@gmail.com'],
                  fail_silently=False
                  )
        return super().form_valid(form)


class RegistrationUser(FormView):
    form_class = RegistrUserForm
    template_name = 'registration.html'
    success_url = reverse_lazy('posts')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user, backend='django.contrib.auth.backends.ModelBackend')
        return super(RegistrationUser, self).form_valid(form)


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


class UserProfile(DetailView):
    model = User
    template_name = 'user_profile.html'

    def get_object(self, queryset=None):
        user = self.request.user
        return user


class ListUser(ListView):
    model = User
    template_name = 'user_list.html'
    context_object_name = 'user_list'
    paginate_by = 5

    def get_queryset(self):
        return User.objects.prefetch_related('post_set')


class CreateComment(CreateView):
    model = Comment
    fields = ('text_comment', 'user_name')
    template_name = 'create_comment.html'

    def form_valid(self, form):
        if self.request.user.is_authenticated:
            Comment.objects.create(user_name=self.request.user.username,
                                   text_comment=form.cleaned_data['text_comment'])
            # отправляет админу письмо
            send_mail('New Comment', f'Пользователь ({self.request.user.username}) создал коментарий ',
                      'django@coment.com',
                      ['orlov229003@gmail.com'])

            send_mail('New Comment', f'({self.request.user.username})добавил/ла новый коментарий',
                      'django@coment.com',
                      [self.request.user.email])
        else:
            Comment.objects.create(user_name=form.cleaned_data["user_name"],
                                   text_comment=form.cleaned_data['text_comment'])
        next_ = self.request.POST.get('next', '/')
        return HttpResponseRedirect(next_)


class ListComments(ListView):
    model = Comment
    template_name = 'comments.html'
    context_object_name = 'comments_list'
    paginate_by = 10


class PostDetail(DetailView):
    model = Post
    template_name = 'one_post.html'
    pk_url_kwarg = 'pk'
    context_object_name = 'post'


class CreatePost(FormView):
    form_class = CreatePosts
    template_name = 'post_form.html'
    success_url = reverse_lazy('posts')
    success_message = 'Post successfully created'

    def form_valid(self, form):
        Post.objects.create(title=form.cleaned_data['title'],
                            short_description=form.cleaned_data['short_description'],
                            image=form.cleaned_data['image'],
                            description=form.cleaned_data['description'],
                            is_published=form.cleaned_data['is_published'],
                            user_id=self.request.user.id)
        send_mail('New Post', f'Пользователь ({self.request.user}) создал пост',
                  self.request.user.email,
                  ['orlov229003@gmail.com'])
        return super().form_valid(form)


class UpdateUserPost(SuccessMessageMixin, UpdateView):
    model = Post
    fields = ["title", "short_description", "image", "description", "is_published"]
    template_name = 'post_form.html'
    success_url = reverse_lazy('user_post')
    success_message = "Profile updated"


class UserPost(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'user_post.html'
    paginate_by = 5

    def get_queryset(self):
        return Post.objects.filter(user=self.request.user)


class UserDetail(DetailView):
    model = User
    template_name = 'user_detail.html'

    def get_object(self, queryset=None):
        user = self.request
        return user


def password_change_done(request):
    logout(request)
    return redirect('login')
