from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Post, Comment, User


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', )


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', )


class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'id', 'status')
    readonly_fields = ('id',)


admin.site.register(User, CustomUserAdmin)
