from django.shortcuts import render, HttpResponse,HttpResponseRedirect
from .models import Post
from .forms import SignUpForm,LoginForm,PostForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout

def product(request):
    posts = Post.objects.all()
    return render(request,'products.html',{'posts' : posts})
def contact(request):
    return render(request,'contact.html')
def about(request):
    return render(request,'#services-container')
def homepage(request):
    return render(request,'homepage.html')
    
def dashboard(request):
    if request.user.is_authenticated:
     posts = Post.objects.all()
     user = request.user
     full_name = user.get_full_name()
     return render(request, 'dashboard.html',{'posts':posts,'full_name':full_name})
    else:
      return HttpResponseRedirect('/login/')

def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')


def user_signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Registration successful')
            form.save()
    else:
            form = SignUpForm()
    return render(request,'signup.html',{'form':form})

def user_login(request):
 if not request.user.is_authenticated:
    if request.method == 'POST':
      form = LoginForm(request=request,data=request.POST)
      if form.is_valid():
       uname = form.cleaned_data['username']
       upass = form.cleaned_data['password']
       user = authenticate(username=uname,password=upass)
       if user is not None:
        login(request,user)
        messages.success(request,'Logged in successfully')
        return HttpResponseRedirect('/dashboard/')
    else:
      form = LoginForm()
    return render(request, 'login.html',{'form':form})
 else:
  return HttpResponseRedirect('/dashboard/')

def addpost(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = PostForm(request.POST)
            if form.is_valid():
                form.save()
                form = PostForm()
        else:
            form = PostForm()
        return render(request,'addpost.html',{'form':form})
    else:
        return HttpResponseRedirect('/login/')

def updatepost(request,id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            pi = Post.objects.get(pk=id)
            form = PostForm(request.POST,instance=pi)
            if form.is_valid():
                form.save()
        else:
            pi = Post.objects.get(pk=id)
            form = PostForm(instance=pi)
        return render(request,'updatepost.html',{'form':form})
    else:
        return HttpResponseRedirect('/login/')

def deletepost(request,id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            pi = Post.objects.get(pk=id)
            pi.delete()
        return render(request,'/dashboard')
    else:
        return HttpResponseRedirect('/login/')

