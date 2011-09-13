from register.models import User
from django.contrib import admin

class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'major', 'year', 'confirmed')

admin.site.register(User, UserAdmin)
