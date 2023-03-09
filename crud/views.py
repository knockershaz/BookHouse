from django.shortcuts import render, HttpResponse,HttpResponseRedirect
from django.shortcuts import get_list_or_404, get_object_or_404
from .models import Post,Order,get_absolute_url
from .forms import SignUpForm,LoginForm,PostForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout

import mysql.connector as sql
un=''
fn=''
ln=''
em=''
pwd=''
t=''
des=''
img=''

# Create your views here.

def user_signup(request):
    global un,fn,ln,em,pwd
    if request.method == 'POST':
        m=sql.connect(host="localhost",user="root",passwd="15081947",database='ApnaMarket')
        cursor=m.cursor()
        d=request.POST
        for key,value in d.items():
            if key=='username':
                un=value
            if key=="first_name":
                fn=value
            if key=="last_name":
                ln=value
            if key=="email":
                em=value
            if key=="password1":
                pwd=value
        
        
        form = SignUpForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Registration successful')
            c="insert into users Values('{}','{}','{}','{}','{}')".format(un,fn,ln,em,pwd)
            cursor.execute(c)
            m.commit()
            form.save()
    else:
            form = SignUpForm()
    return render(request,'signup.html',{'form':form})

def product(request):
    posts = Post.objects.all()
    return render(request,'products.html',{'posts' : posts})
def contact(request):
    return render(request,'contact.html')
def about(request):
    return render(request,'about.html')
def homepage(request):
    return render(request,'homepage.html')

def addfav(request):
    if request.method=="POST":
        book_title = request.POST.get('title')
        order_book=Order.objects.filter(title=book_title).get()
        context = {

        }
        return render(request,'cart.html',context)
    
def dashboard(request):
    if request.user.is_authenticated:
     posts = Post.objects.all()
     user = request.user
     full_name = user.get_full_name()
     return render(request, 'dashboard.html',{'posts':posts,'full_name':full_name})
    else:
      return HttpResponseRedirect('/login/')

def cart(request):
    if request.user.is_authenticated:
        m=sql.connect(host="localhost",user="root",password="Bapan@2002",database='ApnaMarket')
        cursor=m.cursor()
        c="select*from product where fav ='true';"
        cursor.execute(c)
        Orders=tuple(cursor.fetchall())
        # Orders = Order.objects.all()
        user = request.user
        full_name = user.get_full_name()
        return render(request, 'cart.html',{'Orders':Orders})
    else:
      return HttpResponseRedirect('/login/')

def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')

# def user_login(request):
#     global em,pwd
#     if not request.user.is_authenticated():
#         if request.method=="POST":
#             m=sql.connect(host="localhost",user="root",password="15081947",database='ApnaMarket')
#             cursor=m.cursor()
#             d=request.POST
#             for key,value in d.items():
#                 if key=="username":
#                     un=value
#                 if key=="password":
#                     pwd=value
            
#             c="select * from users where username='{}' and password='{}'".format(un,pwd)
#             cursor.execute(c)
#             t=tuple(cursor.fetchall())
#             if t==():
#                 form = LoginForm()
#                 return render(request, 'login.html',{'form':form})
#             else:
#                 return HttpResponseRedirect('/dashboard/')
#     else:
#         return HttpResponseRedirect('/dashboard/')


# def user_login(request):
#  if not request.user.is_authenticated:  
#     if request.method == 'POST':
#       form = LoginForm(request=request,data=request.POST)
#       if form.is_valid():
#        uname = form.cleaned_data['username']
#        upass = form.cleaned_data['password']
#     #    user = authenticate(username=uname,password=upass)
#        m=sql.connect(host="localhost",user="root",password="15081947",database='ApnaMarket')
#        cursor=m.cursor()
#     #    d=request.POST
#     #    for key,value in d.items():
#     #         if key=="username":
#     #             un=value
#     #         if key=="password":
#     #             pwd=value
        
#        c="select * from users where username='{}' and pass='{}'".format(uname,upass)
#        cursor.execute(c)
#        t=tuple(cursor.fetchall()) 
#        if t==():
#         form = LoginForm()
#         return render(request, 'login.html',{'form':form})
#        else:
#         return HttpResponseRedirect('/dashboard/')
#  else:
#   return HttpResponseRedirect('/dashboard/')

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

# def addpost(request):
#     if request.user.is_authenticated:
#         if request.method == 'POST':
#             form = PostForm(request.POST)
#             if form.is_valid():
#                 form.save()
#                 form = PostForm()
#         else:
#             form = PostForm()
#         return render(request,'addpost.html',{'form':form})
#     else:
#         return HttpResponseRedirect('/login/')


# def cart_post(request,id):
#     post=get_object_or_404(Post,id=id)
#     if post.cart.filter(id=request.user.id).exists():
#         post.cart.remove(request.user)
#     else:
#         post.cart.add(request.user)
#     return HttpResponseRedirect(post.get_absoulate_url())    

def addpost(request):
    if request.user.is_authenticated:
        global t,des,img
        if request.method == 'POST':
            form = PostForm(request.POST,request.FILES)
            if form.is_valid():
                # form.save()
                m=sql.connect(host="localhost",user="root",password="Bapan@2002",database='ApnaMarket')
                cursor=m.cursor()
                d=request.POST
                img=form.cleaned_data.get("image")
                for key,value in d.items():
                    if key=="title":
                        t=value
                    if key=="desc":
                        des=value
                    # if key=="image":
                    #     img=value
                # c="insert into users Values('{}','{}','{}','{}','{}')".format(un,fn,ln,em,pwd)        
                c="INSERT into product Values('{}','{}','{}','false');".format(t,des,img)
                cursor.execute(c);
                m.commit();
                posts = Post.objects.all()
                return render(request,'products.html',{'posts' : posts})
                # form = PostForm()
        else:
            form = PostForm()
        return render(request,'addpost.html',{'form':form})
    else:
        return HttpResponseRedirect('/login/')

def addcart(request,title):
            m=sql.connect(host="localhost",user="root",password="Bapan@2002",database='ApnaMarket')
            cursor=m.cursor()
            c="UPDATE product SET fav='true' WHERE title = '{}';".format(title)
            cursor.execute(c)
            posts = Post.objects.all()
            return render(request,'products.html',{'posts' : posts})

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
        return render(request,'deletepost.html')
    else:
        return HttpResponseRedirect('/login/')

