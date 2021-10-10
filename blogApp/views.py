from django.contrib.messages.api import success
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User 
from blogApp.models import Content

# Create your views here.
def index(request):  
    allblogs = Content.objects.all()
    trendBlogs = Content.objects.all().order_by('-pub_date')[:3]
    params = {'allblogs': allblogs,'trendBlogs':trendBlogs}
    return render(request,'index.html',params)

def blogPost(request,slug):
    post = Content.objects.filter(slug=slug).first()
    params = {'post':post}
    return render(request,'blogPost.html',params)

def about(request):
    messages.success(request,"Your Account Has Been Created")
    return render(request,'about.html')

def join_we(request):
    return HttpResponse('This is join we')

def upload_page(request):
    return render(request,'upload.html')

def upload(request):
    if request.method=='POST':
        title = request.POST['title']
        content = request.POST['content']
        category = request.POST['category']
        author = request.POST['author']
        image = request.POST['image']
        
        #creating user
        data_auth= Content(title=title,content=content,category=category,author=author,image=image)        
        data_auth.save()
        messages.success(request,"Your Data Has Been Saved")
        return redirect('/home')
    else:
        return HttpResponse('Not Found')

def sign_up(request):
    if request.method=='POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        uname = request.POST['uname']
        email = request.POST['email01']
        password = request.POST['password']
        birthday = request.POST['birthday']
        
        #creating user
        myuser= User.objects.create_user(uname,email,password)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        messages.success(request,"Your Account Has Been Created")
        return redirect('/home')
    else:
        return HttpResponse('Not Found')

def handleUserLogin(request):
    if request.method== 'POST':
        loginUname = request.POST['loginUname']
        loginPass = request.POST['loginPass']

        user = authenticate(username=loginUname, password=loginPass)

        if user is not None:
            login(request, user)
            messages.success(request,"Successfully Logged In")
            return redirect('/home')

        else:
            messages.error(request, "Invalid Credentials, Please Try Again!!!")
            return redirect('/home')       
    return HttpResponse('404 Not found')

def handleUserLogout(request):
            logout(request)
            messages.success(request,"Successfully Logged Out")
            return redirect('/home')
