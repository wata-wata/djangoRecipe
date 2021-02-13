from django.shortcuts import render
from django.views import View

# Create your views here.


class SiteUserLoginView(View):
    def get(self, request, *args, **kwargs):

        return render(request, "app/siteUser/login.html")


site_user_login = SiteUserLoginView.as_view()
