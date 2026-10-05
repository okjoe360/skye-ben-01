"""
title       : User account view
description : User accounts views
created at  : 04 Oct, 2026
author      : Joel
"""

from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.forms.models import model_to_dict
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login
from accounts.models import Profile
from accounts.forms import RegistrationForm, ProfileForm

def home(request):
    return HttpResponse("Hello, world!")

# User Registration ******************************************************************
def register(request):
    form = RegistrationForm()
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            messages.success(request, "User Created...")
            
            # HTMX ***********************************************************
            if request.headers.get("HX-Request"):
                return render(request, "accounts/partials/register_profile.html", {"form": ProfileForm(), "new_user": model_to_dict(new_user, fields=('id', 'email', 'first_name', 'last_name', 'username'))})
            # HTMX ***********************************************************
            
            return redirect("accounts/register_profile", pk=new_user.id)
    return render(request, "accounts/register.html", {"form": form})


def register_profile(request, pk):
    #new_user = get_object_or_404(User, pk=pk)
    new_user = {'id':1, 'email':'j@j.com', 'first_name':'joel', 'last_name':'okj', 'username':'jokj'}
    form = ProfileForm()
    if request.method == "POST":
        form = ProfileForm(request.POST)
        if form.is_valid():
            user_profile = form.save(commit=False)
            user_profile.user = request.user
            user_profile.save()
            messages.success(request, "User Profile Created...")
            return redirect("dashboard")
    return render(request, "accounts/register_profile.html", {"form": form, "new_user": new_user})
    #return render(request, "accounts/register_profile.html", {"form": form, "new_user": model_to_dict(new_user, fields=('id', 'email', 'first_name', 'last_name', 'username'))})
