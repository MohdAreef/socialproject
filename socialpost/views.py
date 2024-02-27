from django.shortcuts import render,redirect
from django.http import FileResponse,HttpResponse
from django.contrib.auth.models import User
from django.contrib import auth
from .models import *
from datetime import datetime


def home(request):
    all_posts = posts.objects.all() 
    current_date = datetime.now() 
    posts_for_today = posts.objects.filter(date=current_date)
    posts_for_feature=posts.objects.filter(date__gt=current_date) 
    # posts_for_past=posts.objects.filter(date__gt=current_date)
    posts_for_past = posts.objects.filter(date__lt=current_date) 
    # posts_for_past=posts.objects.filter(date__lt=current_date) 
    print(posts_for_past)
    

    data={"all_posts":all_posts,
          "current_date":current_date,
          "posts_for_today":posts_for_today,
          "posts_for_feature":posts_for_feature,
          "posts_for_past": posts_for_past}

    return render(request,"homepage.html",data)

def show1(request):  
    img=open('media/photo3.jpg','rb')
    return FileResponse(img)
def show2(request):
    img=open('media/photo2.png','rb')
    return FileResponse(img)
def show3(request):
    img=open('media/photo1.jpg','rb')
    return FileResponse(img)
# Create your views here.

def signup(request):
  
          
         if request.method=='POST':
           first_name=request.POST.get("first_name")
           last_name=request.POST.get("last_name")
           user_name=request.POST.get("user_name")
           emailaddr=request.POST.get("emailaddr")
           password=request.POST.get("pass")
     
           data=User.objects.create_user(first_name=first_name,last_name=last_name, username= user_name,email=emailaddr,password=password)
           data.save() 
           return redirect('loginform')

 
       

         return render(request,"signupform.html")

def login(request):
    print("hello goood morning")
    if request.method=='POST': 
    
       user_name=request.POST.get("user_name")
       password=request.POST.get("pass")
       user = auth.authenticate(username=user_name, password=password)
       print("inside post")
       if user is not None:
          auth.login(request, user) 
          print("inside valid user") 
        #   print(request.user)
          
        #   request.session['username'] = request.user 
          
          all_posts = posts.objects.all()
          data={"username":user,"all_posts":all_posts}
          return render(request,"userloginpage.html",data) 
        #   return HttpResponse("valid user")
    return render(request,"loginform.html") 

def userloginpage(request):
   print("inside userlogin page")
#    username = request.session.get('username') 
   if request.method == 'GET':
      all_posts = posts.objects.all()
      print("inside user login page")
      user=request.GET.get("username")
      print(user) 
    #    be carefull -------------------------------------- 
      user_instance = User.objects.get(username=user)  
    #   ------------------------
      data={"username":user_instance,"all_posts":all_posts} 
   return render(request,"userloginpage.html",data)   

def createpost(request):  

    data={}
    if request.method=='POST':
        title=request.POST.get("title_name")
        discription=request.POST.get("discription")
        time=request.POST.get("time")
        date=request.POST.get("date")
        # file=request.POST.get("photo")
        file = request.FILES.get('photo') 
        user=request.POST.get("user_name")
        details=request.POST.get("details")
        print("{}{}{}{}{}".format(title,discription,time,date,file))
        new_post=posts()
        new_post.title=title 
        new_post.discription=discription
        new_post.time=time 
        new_post.date=date 
        new_post.details=details 
        new_post.file=file  
        # print("inside createpost")
        # print(user) 
        
          
        user_instance = User.objects.get(username=user)
        print("createpost")
        print(user_instance.username) 
        # new_post.userid=user_instance.username
        new_post.userid=user_instance
        # new_post.file=photo 
        new_post.save() 
        data={'username':user}

    elif request.method=='GET':
        name=request.GET.get('username')
        print("inside elif get method")
        print(name) 
        data={'username':name}

        
    return render(request,"createpost.html",data) 

def deletepost(request):
    if request.method=='GET':
       username = request.GET.get('username')
       post_id = request.GET.get('post_id')
       delepost = posts.objects.get(id=post_id)
       delepost.delete() 
       print(username)
       all_posts = posts.objects.all()
       user_instance = User.objects.get(username=username)
       data={"username":user_instance,"all_posts":all_posts} 
    return render(request,"userloginpage.html",data)   
   

def logoutsession(request):
    print("logout")
    all_posts = posts.objects.all() 
    current_date = datetime.now() 
    posts_for_today = posts.objects.filter(date=current_date)
    posts_for_feature=posts.objects.filter(date__gt=current_date)

    data={"all_posts":all_posts,"current_date":current_date,"posts_for_today":posts_for_today,"posts_for_feature":posts_for_feature}
   
    return render(request,"homepage.html",data)

def changepassword(request):

    if request.method=='GET':
      username=request.GET.get('username') 
      data={"username":username}
      return render(request,"changepassword.html",data)
    
    elif request.method=='POST':
        username=request.POST.get('username')
        new_password=request.POST.get('pass')
        user = User.objects.get(username=username) 
        user.set_password(new_password) 
        user.save() 

        all_posts = posts.objects.all() 
        user_instance = User.objects.get(username=username)
        data={"username":user_instance,"all_posts":all_posts} 
        return render(request,"userloginpage.html",data)   
    

        # return HttpResponse(username)
def moredetails(request):

   if request.method == 'GET':
      postid=request.GET.get('postid')
      post = posts.objects.get(id=postid)
      name=post.title
      print("hellondmm") 
      print(name)
      data={'post':post}
    # return HttpResponse(name)

      return render(request,"moredetails.html",data)
    
    
