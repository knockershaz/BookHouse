"""eCommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path,include
from crud import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('ckeditor/',include('ckeditor_uploader.urls')),
    path('admin/', admin.site.urls),
    path('',views.homepage,name="homepage"),
    path('home/',views.homepage,name="homepage"),
    path('about/',views.about,name="about"),
    path('contact/',views.contact,name="contact"),
    path('product/',views.product,name="product"),
    path('signup/',views.user_signup,name="user_signup"),
    path('signin/',views.user_login,name="user_login"),
    path('dashboard/',views.dashboard,name="dashboard"),
    path('cart/',views.cart,name="cart"),
    path('addpost/',views.addpost,name="addpost"),
    path('updatepost/<int:id>',views.updatepost,name="updatepost"),
    path('deletepost/<int:id>',views.deletepost,name="deletepost"),
    path('logout/',views.user_logout,name="logout"),
    path('oauth/', include('social_django.urls', namespace='social')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)