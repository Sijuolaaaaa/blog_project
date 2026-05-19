from django.shortcuts import render, redirect,get_object_or_404
from django.views import generic
from django.urls import reverse_lazy
from .forms import SignupForm, ProfileForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .models import Profile
from postApp.models import UserPost



# Create your views here.

class SignupView(generic.CreateView):
    form_class = SignupForm
    template_name = "registration/signup.html"
    success_url = reverse_lazy("login")

@login_required
def profileView(request):
    blogPosts = UserPost.objects.filter(author=request.user).order_by("created_at")

    profile,created = Profile.objects.get_or_create(author=request.user)
    return render(
            request, 
            template_name="profile.html",
            context= {
                "profile": profile,
                "blogPosts": blogPosts
                }
            )

@login_required
def editProfileView(request):
    profile = request.user.profile

    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile')

    else:
        form = ProfileForm(instance=profile)

    return render(
        request, 
        template_name="editProfile.html",
         context= {
             "form": form
             }
        )