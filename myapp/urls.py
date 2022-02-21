from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from .views import *
from django.contrib.auth.views import PasswordChangeView

urlpatterns = [
    path('home/', Home.as_view(), name='home_page'),

    path('posts/', AllPosts.as_view(), name='posts'),
    path('post_detail/<pk>', PostDetail.as_view(), name='post_detail'),
    path('create_posts/', CreatePost.as_view(), name='create_post'),

    path('users/', ListUser.as_view(), name='user_list'),
    path('update/', UpdateProfile.as_view(), name='update'),
    path('update_user_post/<int:pk>', UpdateUserPost.as_view(), name='update_user_post'),
    path('user_detail_profile/', UserProfile.as_view(), name='user_profile'),
    path('user_detail/', UserDetail.as_view(), name='user_detail'),
    path('user_post/', UserPost.as_view(), name='user_post'),

    path('list_comments/', ListComments.as_view(), name='list_comments'),
    path('create_comment/', CreateComment.as_view(), name='create_comment'),

    path('message_admin/', message_admin_form, name='message_admin'),

    path('registration/', RegistrationUser.as_view(), name='registr'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
