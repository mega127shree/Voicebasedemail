from django.contrib import admin
from .models import UserDetails
from .models import LoginDetails
# Register your models here.

admin.site.register(UserDetails)
admin.site.register(LoginDetails)