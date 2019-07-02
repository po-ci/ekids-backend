from stockApi import settings
from ..Types.UserType import UserType
from ..Models.User import User
import graphene


class MeQuery(graphene.ObjectType):
    me = graphene.Field(UserType)

    def resolve_me(self, info):
        user = info.context.user
        if user.is_anonymous:
            raise Exception('Not logged in!')
        if user.avatar:
            user.avatar.image = settings.MEDIA_HOST + user.avatar.image.name
        return user
