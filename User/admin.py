from django.contrib import admin
from .models import User

class UserAdmin(admin.ModelAdmin):
    list_display = ('user_name', 'email_id', 'user_type')

admin.site.register(User, UserAdmin)
