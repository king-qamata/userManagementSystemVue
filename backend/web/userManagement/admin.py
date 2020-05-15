from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser, Profile


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    exclude = ['date_joined']
    model = CustomUser
    list_display = ['email', 'username', 'is_active','is_staff',]

#class UserAdmin(admin.ModelAdmin):
    #list_display = ['email', 'username', 'is_active','is_staff',]


admin.site.register(CustomUser, CustomUserAdmin)
#admin.site.register(CustomUser, UserAdmin)
admin.site.register(Profile)