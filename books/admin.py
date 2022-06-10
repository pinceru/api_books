from django.contrib import admin
from books.models import User

class Users(admin.ModelAdmin):
    list_display = ('id', 'name', 'last_name', 'telephone', 'email')
    list_display_links = ('id', 'name',)

admin.site.register(User, Users)