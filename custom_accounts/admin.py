from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from custom_accounts.models import User
from base.models import UserProfile
from django.utils.html import format_html

# Register your models here.

class UserAdmin(UserAdmin):
    def thumbnail(self, object):
        return format_html('<img src="{}" width="50" style="border-radius:20%;">'.format(object.avatar.url))
    thumbnail.short_description = 'Avatar'
    list_display=('thumbnail','email','username','date_joined','is_active',)
    list_display_links=('thumbnail','email','username',)
    readonly_fields=('date_joined',)
    ordering = ('-date_joined',)
    filter_horizontal=()
    list_filter = ('email',)
    fieldsets=()
    
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ( 'user', 'credits', 'free_credits','date',)
    list_display_links=('user','date',)
    ordering = ('user',)
    filter_horizontal = ()
    list_filter = ('user',)
    fieldsets = ()

admin.site.register(User, UserAdmin)
admin.site.register(UserProfile, UserProfileAdmin)
