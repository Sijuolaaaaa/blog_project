from django.shortcuts import render
from .models import UserPost

# Create your views here.
def homeView(request):
    blogPosts = UserPost.objects.filter(status= "PUBLISH")

    return render(
        request,
        template_name= "index.html",
        context= {"blogPosts": blogPosts}
    )
