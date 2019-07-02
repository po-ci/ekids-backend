from ..models import User
from graphene_django import DjangoObjectType
from graphene import relay, AbstractType, ObjectType


class UserNode(DjangoObjectType):
    class Meta:
        model = User
        filter_fields = {
            'id': ['exact'],
            'username': ['exact', 'icontains', 'istartswith'],
        }
        interfaces = (relay.Node,)
