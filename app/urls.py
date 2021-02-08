from django.urls import path
from . import views


app_name='app'
urlpatterns = [
    path('siteUser/login', views.site_user_login, name='site_user_login'),
]