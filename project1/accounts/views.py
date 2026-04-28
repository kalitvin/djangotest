from django.contrib.auth import login
from django.shortcuts import render, redirect, get_object_or_404
from .forms import SignUpForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Profile



def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("post_list")
    else:
        form = SignUpForm()
    return render(request, "registration/signup.html", {"form": form})


@login_required
def profile_view(request, username=None):
    if username is None:
        user = request.user
    else:
        user = get_object_or_404(User, username=username)

    profile, _ = Profile.objects.get_or_create(user=user)

    context = {
        "profile_user": user,
        "profile": profile,
    }
    return render(request, "accounts/profile.html", context)

@login_required
def profile_edit(request):
    profile, _ = Profile.objects.get_or_create(user=request.user)

    if request.method == "POST":
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(
            request.POST,
            request.FILES,  # важно
            instance=profile,
        )
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            return redirect("profile")
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=profile)

    context = {"u_form": u_form, "p_form": p_form}
    return render(request, "accounts/profile_edit.html", context)