from django.contrib import admin
from accounts.models import User, License, Rating


admin.site.register(License)
admin.site.register(Rating)

class UserAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'license_number']


admin.site.register(User, UserAdmin)