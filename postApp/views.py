from django.shortcuts import render, get_object_or_404, redirect
from .models import UserPost
from django.contrib.auth.decorators import login_required


# Create your views here.
def homeView(request):
    blogPosts = UserPost.objects.all()[:4]

    return render(
        request,
        template_name= "index.html",
        context= {"blogPosts": blogPosts}
    )

def archiveView(request):
    blogPosts = UserPost.objects.filter(status="PUBLISH")

    return render(
        request,
        template_name= "archives.html",
        context= {"blogPosts": blogPosts}
    )

def singleBlogView(request, blog_id):
    blogPost = get_object_or_404(UserPost, id=blog_id)
    
    return render(
        request,
        template_name='read_more.html',
        context={'blogPost': blogPost}
    )

@login_required
def deleteBlogView(request, blog_id):
    blog = get_object_or_404(UserPost, id=blog_id)
    blog.delete()
    return redirect("home")

