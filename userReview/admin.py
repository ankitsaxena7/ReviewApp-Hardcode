from django.contrib import admin
from .models import Users, Review

# Register your models here.
@admin.register(Users)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name','last_name','email','password','gender','createdate',]


@admin.register(Review)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'users','rating','reviewto','reviewdesc','reviewdate']