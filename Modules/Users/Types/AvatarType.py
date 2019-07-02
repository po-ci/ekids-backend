from ..models import Avatar
from graphene_django import DjangoObjectType


class AvatarType(DjangoObjectType):
    class Meta:
        model = Avatar
