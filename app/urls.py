from django.urls import path
from . import views


app_name = "app"
urlpatterns = [
    path("siteUser/login", views.site_user_login, name="site_user_login"),
    path("siteUer/logout", views.site_user_logout, name="site_user_logout"),
    path("siteUser/register", views.site_user_register, name="site_user_register"),
    path("siteUser/profile", views.site_user_profile, name="site_user_profile"),
]
