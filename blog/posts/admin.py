from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import Post, Comment

admin.site.unregister(User)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', )


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', )


class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'id')
    readonly_fields = ('id',)


admin.site.register(User, CustomUserAdmin)
