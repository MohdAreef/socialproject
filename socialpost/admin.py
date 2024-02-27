from django.contrib import admin


from .models import *
class ServiceAdmin(admin.ModelAdmin):
         list_display=("title","discription","date","time","file")
#Register your model here 
admin.site.register(posts,ServiceAdmin)
# Register your models here.
