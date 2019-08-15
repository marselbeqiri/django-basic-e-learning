from django.contrib import admin
from .models import Choice, Question #, Comment

from django.contrib.auth.models import Group 

# Register your models here.
admin.site.site_header = 'Admin Dashboard'

admin.site.register(Question)
admin.site.register(Choice)
#admin.site.register(Comment)