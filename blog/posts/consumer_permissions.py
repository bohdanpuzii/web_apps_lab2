from djangochannelsrestframework.permissions import BasePermission
from django.contrib.auth.models import AnonymousUser
from .models import Post, Comment


def is_user_logged_in(user):
    return not isinstance(user, AnonymousUser)


class PostPermissions(BasePermission):
    def has_permission(self, scope, consumer, action, **kwargs):
        if action == 'list':
            return True
        try:
            if action == 'delete' and Post.objects.filter(pk=kwargs.get('pk')).first().author == scope['user']:
                return True
        except AttributeError:
            return True
        if action == 'create' and is_user_logged_in(scope['user']):
            return True


class CommentPermissions(BasePermission):
    def has_permission(self, scope, consumer, action, **kwargs):
        if action == 'retrieve':
            return True
        try:
            if action == 'delete' and Comment.objects.filter(pk=kwargs.get('pk')).first().creator == scope['user'] \
                    or scope['user'].is_superuser:
                return True
        except AttributeError:
            return True
        if action == 'create' and is_user_logged_in(scope['user']):
            return True
