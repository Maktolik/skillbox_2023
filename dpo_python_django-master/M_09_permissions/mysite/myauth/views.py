from django.contrib.auth.decorators import login_required, permission_required, user_passes_test
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LogoutView
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect, reverse
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView

from .models import Profile


class AboutMeView(TemplateView):
    template_name = "myauth/about-me.html"


class RegisterView(CreateView):
    form_class = UserCreationForm
    template_name = "myauth/register.html"
    success_url = reverse_lazy("myauth:about-me")

    def form_valid(self, form):
        response = super().form_valid(form)
        Profile.objects.create(user=self.object)

        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password1")
        user = authenticate(self.request, username=username, password=password)
        login(request=self.request, user=user)

        return response


def login_view(request: HttpRequest) -> HttpResponse:
    if request.method == "GET":
        return redirect('/admin/')
    return render(request, 'myauth/login.html')


    username = request.POST("username")
    password = request.POST("password")

    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect('/admin/')

    return (request, 'myauth/login.html', {"error":"Invalid login creadentials"})


# def logout_view(request: HttpRequest) -> HttpResponse:
#     logout(request)
#     return redirect(reverse("myauth:login"))
#

class MyLogoutView(LogoutView):
    next_page = reverse_lazy("myauth:login")

# class LogoutAcceptView(MyLogoutView):
#     template_name = 'myauth/logout-accept.html'
#
#     def get(self, request: HttpRequest):
#         response = logout(request)
#         return render(response, self.template_name)

@user_passes_test(lambda u: u.is_superuser)
def set_cookie_view(request: HttpRequest) -> HttpResponse:
    response = HttpResponse("Cookie set")
    response.set_cookie("fizz", "buzz", max_age=3600)
    return response


def get_cookie_view(request: HttpRequest) -> HttpResponse:
    value = request.COOKIES.get("fizz", "default value")
    return HttpResponse(f"Cookies value: {value!r}")


@permission_required("myauth.view_profile", raise_exception=True)
def set_session_view(request: HttpRequest) -> HttpResponse:
    request.session["foobar"]="spammegs"
    return HttpResponse("Session set!")


@login_required
def get_session_view(request: HttpRequest) -> HttpResponse:
    value = request.session.get("foobar", "default")
    return HttpResponse(f"Session value{value!r}!")





