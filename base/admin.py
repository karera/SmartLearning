#Admin
#=> admin
#=> karachi12 (password)
#=> mehfooz.connect@gmail.com (email)
#New Windows codes

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from base.models import Course, Tag, Prerequisite, Learning, Video
from django.utils.html import format_html

# Register your models here.


class TagAdmin(admin.TabularInline):
    model = Tag

class VideoAdmin(admin.TabularInline):
    model = Video

class LearningAdmin(admin.TabularInline):
    model = Learning

class PrerequisiteAdmin(admin.TabularInline):
    model = Prerequisite

class CourseAdmin(admin.ModelAdmin):
    inlines = [TagAdmin , LearningAdmin , PrerequisiteAdmin , VideoAdmin]
    def course_thumbnail(self, object):
        return format_html('<img src="{}" width="80" height="80" style="border-radius:5px;">'.format(object.thumbnail.url))
    course_thumbnail.short_description = 'Thumbnail'

    list_display=('course_thumbnail','id','name', 'category', 'sub_category' , 'active', 'date',)
    list_display_links=('course_thumbnail','name',)
    readonly_fields=('date',)
    ordering = ('date',)
    filter_horizontal=()
    list_filter = ("category", 'sub_category' , 'active',)
    fieldsets=()

admin.site.register(Video)
admin.site.register(Course , CourseAdmin)





