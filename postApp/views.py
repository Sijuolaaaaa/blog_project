from django.shortcuts import render, get_object_or_404, redirect
from .models import UserPost
from django.contrib.auth.decorators import login_required
from .forms import Blogform
from django.contrib import messages


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
    blog = get_object_or_404(UserPost, id=blog_id, author=request.user)

    if request.method == "POST":
        blog.delete()
        messages.success(request, "Blog deleted successfully.")
        return redirect("home")

    return render(
        request,
        template_name="deleteBlog.html",
        context={
            "blog": blog
        }
    )

def aboutView(request):
    return render(
        request,
        template_name= "about.html",
        context= {}
    )

@login_required
def editBlogView(request, blog_id):
    blogPost= get_object_or_404(UserPost, id=blog_id)
    if request.method == "POST":
        form= Blogform(request.POST, request.FILES, instance=blogPost)
        if form.is_valid():
            form.save()
            messages.success(request, 'blog edited successfully')
        else:
            messages.error(request, 'An error occurred while editing blog')
        return redirect("single_blog", blogPost.id)
    else:
        form= Blogform(instance=blogPost)
        return render(
            request,
            template_name="blogform.html",
            context={
                "Action": "Edit",
                "form": form
                }
        )

@login_required
def addBlogView(request):
    if request.method == "POST":
        form= Blogform(request.POST, request.FILES)
        if form.is_valid():
            blog=form.save(commit=False)
            blog.author= request.user
            blog.save()
            messages.success(request, 'blog added successfully')
            return redirect("home")
        else:
            messages.error(request, 'An error occurred while creating post')
        return redirect("addBlog")

    else:
        form= Blogform()
        return render(
            request,
            template_name="blogform.html",
            context={"form": form}
        )