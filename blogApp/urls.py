from os import stat
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='index'),
    path('home',views.index,name='index'),
    path('about',views.about,name='index'),
    path('join_we',views.join_we,name='index'),
    path('sign_up',views.sign_up,name='sign_up'),
    # path('log_in',views.log_in,name='log_in'),
    path('login',views.handleUserLogin,name='handleUserLogin'),
    path('logout',views.handleUserLogout,name='handleUserLogOut'),
    path('upload_page',views.upload_page,name='upload'),
    path('<str:slug>',views.blogPost,name='blogPost')
    
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
