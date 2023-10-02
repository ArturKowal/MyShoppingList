from django.contrib import admin
from .models import Room, User

# admin.register(User)
# admin.register()

# class AuthorAdmin(admin.ModelAdmin):
#     pass


admin.site.register(User)
admin.site.register(Room)
