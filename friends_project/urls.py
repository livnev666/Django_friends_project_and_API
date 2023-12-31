"""friends_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from friends_app.viewsAPI import *
from rest_framework import routers

admin.site.site_header = 'Наша админка'
admin.site.index_title = 'Моя панель управления кораблем'

router = routers.DefaultRouter()
router.register(r'friends_app', MovieAPIListCreate)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('__debug__/', include('debug_toolbar.urls')),
    path('captcha/', include('captcha.urls')),

    path('', include('friends_app.urls')),

    # Авторизация по сессии
    path('api/v1/friends-auth/', include('rest_framework.urls')),

    # Регистрация пользователя
    path('api/v1/auth/', include('djoser.urls')),
    # Авторизация по токенам. И в запросе адрес будет auth/token/login/
    re_path(r'^auth/', include('djoser.urls.authtoken')),


    path('api/v1/friends/', MovieAPIListCreate.as_view()),
    path('api/v1/friends/<int:pk>/', MovieAPIUpdate.as_view()),
    path('api/v1/friendsdelete/<int:pk>/', MovieAPIDelete.as_view()),

    path('api/v1/friends/comment/', CommentAPIListCreate.as_view()),
    path('api/v1/friends/comment/<int:pk>/', CommentAPIUpdate.as_view()),
    path('api/v1/friendsdelete/comment/<int:pk>/', CommentAPIDelete.as_view()),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
