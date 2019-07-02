from ..models import Avatar
from graphene_django import DjangoObjectType
from graphene import relay, AbstractType, ObjectType


class AvatarNode(DjangoObjectType):
    class Meta:
        model = Avatar
        filter_fields = {
            'id': ['exact'],
        }
        interfaces = (relay.Node,)
