from django.contrib import admin
from users.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

class UserAdmin(BaseUserAdmin):
    model = User
    list_display = ['email', 'id']
    search_fields = ['email']

admin.site.register(User, UserAdmin)