from django.contrib import admin
from .models import Administrator, Moderator


admin.site.register(Administrator)
admin.site.register(Moderator)

# Register your models here.
