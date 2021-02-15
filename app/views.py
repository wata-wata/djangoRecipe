from django.shortcuts import render, redirect
from django.views import View
from .forms import SiteUserRegisterForm, SiteUserLoginForm
from django.contrib import messages
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.


class SiteUserLoginView(View):
    def get(self, request, *args, **kwargs):
        context = {
            "form": SiteUserLoginForm(),
        }
        return render(request, "app/siteUser/login.html", context)

    def post(self, request, *args, **kwargs):
        form = SiteUserLoginForm(request.POST)
        if not form.is_valid():
            return render(request, "app/siteUser/login.html", {"form": form})

        login_site_user = form.get_site_user()

        auth_login(request, login_site_user)

        messages.success(request, "ログインしました")

        return redirect("app:site_user_profile")


site_user_login = SiteUserLoginView.as_view()


class SiteUserLogoutView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):

        if request.user.is_authenticated:
            auth_logout(request)

        messages.success(request, "ログアウトしました")

        return redirect("app:site_user_login")


site_user_logout = SiteUserLogoutView.as_view()


class SiteUserRegisterView(View):
    def get(self, request, *args, **kwargs):
        context = {
            "form": SiteUserRegisterForm(),
        }
        return render(request, "app/siteUser/register.html", context)

    def post(self, request, *args, **kwargs):
        form = SiteUserRegisterForm(request.POST)
        if not form.is_valid():
            return render(request, "app/siteUser/register.html", {"form": form})

        new_site_user = form.save(commit=False)
        new_site_user.set_password(form.cleaned_data["password"])

        new_site_user.save()
        messages.success(request, "会員登録が完了しました")
        return redirect("app:site_user_login")


site_user_register = SiteUserRegisterView.as_view()


class SiteUserProfileView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):

        return render(request, "app/siteUser/profile.html")


site_user_profile = SiteUserProfileView.as_view()
