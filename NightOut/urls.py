from django.urls import re_path as url
from django.urls import path, re_path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'NightOut'

print(settings.STATIC_ROOT)
urlpatterns = [
    path('', views.home, name='home'),
    re_path(r'^home/$', views.home, name='home'),
    path('login', views.login, name='login'),
    path('create_event', views.create_event, name='create_event')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)