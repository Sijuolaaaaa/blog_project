"""
URL configuration for blog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from postApp.views import homeView, archiveView, singleBlogView, deleteBlogView, aboutView, editBlogView, addBlogView
from django.conf import settings
from django.conf.urls.static import static
from userApp.views import SignupView, profileView, editProfileView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homeView, name='home'),
    path('archives', archiveView, name='archives'),
    path('single_blog/<int:blog_id>/', singleBlogView, name='single_blog'),
    path('delete_blog/<int:blog_id>/', deleteBlogView, name='delete_blog'),
    path('profile', profileView, name='profile'),
    path("accounts/", include('django.contrib.auth.urls')),
    path("signup/", SignupView.as_view(), name='signup'),
    path('profile/', profileView, name='profile'),
    path('editProfile/', editProfileView, name='editProfile'),
    path('about/', aboutView, name='about'),
    path("edit_blog/<int:blog_id>/", editBlogView, name= "edit_blog"),
    path("addBlog/", addBlogView, name="addBlog"),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

