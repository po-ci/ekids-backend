import graphql_jwt

from stockApi import settings
from ..Types.UserType import UserType
import graphene


class ObtainJSONWebToken(graphql_jwt.JSONWebTokenMutation):
    user = graphene.Field(UserType)

    @classmethod
    def resolve(cls, root, info, **kwargs):
        if info.context.user.avatar:
            info.context.user.avatar.image = settings.MEDIA_HOST + info.context.user.avatar.image.name
        return cls(user=info.context.user)
