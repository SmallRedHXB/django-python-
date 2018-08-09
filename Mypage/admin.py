#encoding=utf-8
from django.contrib import admin

from .models import Users, Userinfo, Teacherinfo, Courseinfo

# Register your models here.

admin.site.register(Users)
admin.site.register(Userinfo)
admin.site.register(Teacherinfo)
admin.site.register(Courseinfo)