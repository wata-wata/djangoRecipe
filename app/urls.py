from django.urls import path
from . import views

app_name = 'djangoRecipe'
urlpatterns = [
	path("siteUser/login", views.SiteUserLoginView.as_view(), name="site_user_login"),
	path('',views.IndexView.as_view(),name='index'),
	path('result',views.ResultView.as_view(),name='result')
]