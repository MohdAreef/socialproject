from django.db import models
from django.contrib.auth.models import User

# def default_file():
#     return 'media/photo1.jpg'


# Create your models here.
class posts(models.Model):
    title=models.CharField(max_length=10)
    discription=models.TextField()
    details=models.TextField(null=True)
    date=models.DateField()
    time=models.TimeField() 
    
    file=models.FileField(upload_to='postsimage/',max_length=250,null=True,default=None) 
    # file = models.FileField(upload_to='media', default=default_file)


     # Foreign key referencing the User table
    userid = models.ForeignKey(User, on_delete=models.CASCADE,to_field='username')
