from django.contrib import admin

from .models import Blog,Comment

class blogAdmin(admin.ModelAdmin):
    list_display=('id','blog_title','blog_content','created_at','upload_to')
    search_fields=['blog_title']

admin.site.register(Blog,blogAdmin)

class CommentAdmin(admin.ModelAdmin):
    list_display=('id','blog','comment_title','created_at')
    search_fields=['blog_title']

admin.site.register(Comment,CommentAdmin)