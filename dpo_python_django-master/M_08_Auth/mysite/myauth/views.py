from django.contrib.auth.views import LogoutView
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect, reverse
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse_lazy


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


def set_cookie_view(request: HttpRequest) -> HttpResponse:
    response = HttpResponse("Cookie set")
    response.set_cookie("fizz", "buzz", max_age=3600)
    return response


def get_cookie_view(request: HttpRequest) -> HttpResponse:
    value = request.COOKIES.get("fizz", "default value")
    return HttpResponse(f"Cookies value: {value!r}")


def set_session_view(request: HttpRequest) -> HttpResponse:
    request.session["foobar"]="spammegs"
    return HttpResponse("Session set!")


def get_session_view(request: HttpRequest) -> HttpResponse:
    value = request.session.get("foobar", "default")
    return HttpResponse(f"Session value{value!r}!")





