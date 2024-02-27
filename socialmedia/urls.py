"""
URL configuration for socialmedia project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
from socialpost import views 

# new added

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls), 
    path('',views.home), 
    path('show1',views.show1),
    path('show2',views.show2), 
    path('show3',views.show3), 
    path('signupform',views.signup),
    path('loginform',views.login,name='loginform'),
    path('userloginpage',views.userloginpage,name='userloginpage'),
    path('createpost',views.createpost,name="createpost"),
    path('deletepost',views.deletepost,name="deletepost"),
    path('logout',views.logoutsession), 
    path('changepassword',views.changepassword,name="changepassword"),
    path('moredetails',views.moredetails,name='moredetails')
]

# new added
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
# urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) 
    