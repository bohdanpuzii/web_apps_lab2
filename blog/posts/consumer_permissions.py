from djangochannelsrestframework.permissions import BasePermission
from django.contrib.auth.models import AnonymousUser
from asgiref.sync import sync_to_async
from .models import Post


class PostPermissions(BasePermission):
    def has_permission(self, scope, consumer, action, **kwargs):
        if action == 'list':
            return True
        try:
            if action == 'delete' and Post.objects.filter(pk=kwargs.get('pk')).first().author == scope['user']:
                return True
        except AttributeError:
            return True
        if action == 'create' and not isinstance(scope['user'], AnonymousUser):
            return True