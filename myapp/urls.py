from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import *

urlpatterns = [
    path('home/', Home.as_view(), name='home_page'),
    path('posts/', AllPosts.as_view(), name='posts'),
    path('post_detail/<pk>', PostDetail.as_view(), name='post_detail'),
    path('user_detail/<pk>', UserProfile.as_view(), name='user_detail'),
    path('create_posts/', CreatePost.as_view(), name='create_post'),
    path('message_admin/', MessageAdmin.as_view(), name='message_admin'),
    path('registration/', RegistrationUser.as_view(), name='registr'),
    path('update/', UpdateProfile.as_view(), name='update'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
