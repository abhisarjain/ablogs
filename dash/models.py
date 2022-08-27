import ipaddress
from django.db.models.deletion import CASCADE
from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.
from django.conf import settings
from django.contrib.auth.models import AbstractUser, auth

class Contact(models.Model):
    name_cu = models.CharField(max_length=20)
    mail_cu = models.EmailField(max_length=40)
    feedback = models.TextField()


    def __str__(self):
        return self.name_cu


class Profile(AbstractUser):
     bio = models.TextField()
     dp = models.ImageField(upload_to='dash/images',default="")
     otp = models.CharField(max_length=6)



class Blog(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=20)
    desc = models.TextField()
    author = models.CharField(max_length=20)
    image = models.ImageField(upload_to='dash/images',default="")
    date = models.DateTimeField(auto_now_add=True)
    views = models.IntegerField(default=0)
    # ipadd = models.CharField(max_length=50)


    def __str__(self):
        return self.title
    
class ipaddress(models.Model):
    blog = models.ForeignKey(Blog,on_delete=models.CASCADE)
    ipadd = models.CharField(max_length=50)

    def __str__(self):
        return self.ipadd

class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,null=True,blank=True)
    blog = models.ForeignKey(Blog,on_delete=models.CASCADE)
    comments = models.TextField()
    def __str__(self):
        return (self.blog.title)

class Chat(models.Model):
    sender = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,related_name='sender')
    reciever = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,related_name='reciever')
    message = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.message
    # def get_num_likes(self):
    #     return self.liked.all().count()
        #  liked = models.ManyToManyField(settings.AUTH_USER_MODEL,related_name='liked')


class News(models.Model):
    news_title = models.CharField(max_length=100)
    news_link = models.CharField(max_length=100,default="none")
    def __str__(self):
        return self.news_title