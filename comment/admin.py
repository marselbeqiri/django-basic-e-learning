from django.contrib import admin
from .models import  Comment_Poll, Comment_main
# Register your models here.

admin.site.register(Comment_main)
admin.site.register(Comment_Poll)