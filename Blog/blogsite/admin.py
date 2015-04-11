from django.contrib import admin
from blogsite.models import BlogPost, Comment


class CommentInline(admin.StackedInline):
    model = Comment
    extra = 1

class BlogPostAdmin(admin.ModelAdmin):
    list_display = ['title', 'timestamp']
    list_display_links = ['title', 'timestamp']
    list_filter = ['title', 'timestamp']
    inlines = [CommentInline]
    

admin.site.register(BlogPost, BlogPostAdmin)