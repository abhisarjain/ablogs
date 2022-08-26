from django.contrib import admin
from django.contrib.admin.decorators import register
from .models import Profile,Contact,Blog,Chat,News,ipaddress,Comment
from django.contrib.auth.admin import UserAdmin
# Register your models here.
admin.site.register(Profile)
admin.site.register(Contact)
admin.site.register(Blog)
admin.site.register(Chat)
admin.site.register(News)
admin.site.register(ipaddress)
admin.site.register(Comment)