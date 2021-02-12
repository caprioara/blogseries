from django.contrib import admin
from . import models
from mptt.admin import MPTTModelAdmin

@admin.register(models.Post)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('title', 'id', 'status', 'slug', 'author')
    prepopulated_fields = {
        "slug": ("title",), }

admin.site.register(models.Category)
admin.site.register(models.Comment, MPTTModelAdmin)

# @admin.register(models.Comment)
# class CommentAdmin(admin.ModelAdmin):
#     list_display = ('post', 'name', 'email', 'publish','status')
#     list_filter = ('status', 'publish')
#     search_field = ('name', 'email', 'content')



# class AuthorAdmin(admin.ModelAdmin):
#     list_display = ('title', 'status', 'slug', 'author')

# admin.site.register(models.Post, AuthorAdmin)