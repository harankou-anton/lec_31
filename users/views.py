from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import redirect, render

from users.forms import RegisterForm, LoginForm
from users.models import User


def register(request):
    form = RegisterForm()
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():

            user = User(email=form.cleaned_data["email"])
            user.set_password(form.cleaned_data["password"])
            user.save()
            return redirect("/")
    else:
        form = RegisterForm()

    return render(request, "register.html", {"form": form})

def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(request=request,
                                email=form.cleaned_data["email"],
                                password=form.cleaned_data["password"],)
            if user is None:
                return HttpResponse('BadRequest', status=400)
            login(request, user)
            return redirect("/")
    else:
        form = LoginForm()
    return render(request, "login.html", {"form": form})