from django.contrib import admin
from .models import Users

class UsersAdmin(admin.ModelAdmin):
    list_display = ('UserId', 'User_Name', "Password")

# Register your models here.
    
admin.site.register(Users, UsersAdmin)

