import requests
import json
from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.template.loader import render_to_string
from django.http import HttpResponse, JsonResponse
from django.core.mail import send_mail, BadHeaderError
from django.contrib import messages, auth


def signup(request):
    form = SignupForm()
    context = {"form": form}
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            password = form.cleaned_data["password"]
            user.set_password(password)
            user.save()
            print('user saved')
            messages.success(request, 'Account created successfully')
            return redirect('/accounts/login')
        else:
            error = form.errors
            print('error = ',error)
            form = SignupForm()
            context = {"form": form}
            messages.warning(request, error)
            return render(request, "accounts/signup.html", context)
    else:
        form = SignupForm()
    context = {"form": form}
    return render(request, "accounts/signup.html", context)

def login(request):
    print('login')
    if "username" in request.session:
        print('if')
        return redirect("/")
    elif request.method == "POST":
        print('elif')
        username = request.POST["username"]
        password = request.POST["password"]
        user = auth.authenticate(username=username, password=password)
        user_created = ExtendUser.objects.get(username=username)
        if user is not None:
            auth.login(request, user)
            request.session["username"] = username
            messages.success(request, "loggedin successfully")
            return redirect("home")
        elif user_created.is_active == False:
            messages.warning(request, "Email verification pending")
            return render(request, "accounts/login.html")
        else:
            messages.warning(request, "Username or password is incorrect!")
            return render(request, "accounts/login.html")
    else:
        print('else')
        return render(request, "accounts/login.html")

def logout(request):
    auth.logout(request)
    username = request.session.get("username")
    del username
    return render(request, "accounts/logout.html")
