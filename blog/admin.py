from django.contrib import admin
from .models import Post, Comment, ContactEnquiry
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    """
    Represents the Post model in the Django Admin Interface
    """

    list_display = ('title', 'slug', 'status', 'created_on')
    search_fields = ['title', 'content']
    list_filter = ('status', 'created_on')
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """
    Represents the Comment model in the Django Admin Interface
    """
    list_display = ('name', 'body', 'post', 'created_on', 'approved')
    list_filter = ('approved', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        """
        Adds approval action to drop-down list
        """
        queryset.update(approved=True)


@admin.register(ContactEnquiry)
class ContactAdmin(admin.ModelAdmin):
    """
    Represents the ContactEnquiry model in the Django Admin Interface
    """
    list_display = ('name', 'email', 'subject', 'created_on', 'completed')
    actions = ['completed']
    list_filter = ('completed', 'created_on')
    search_fields = ('name', 'email', 'message')
    summernote_fields = ('content',)
