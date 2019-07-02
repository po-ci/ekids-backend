from stockApi import settings
from ..Types.UserType import UserType
from ..Models.User import User
import graphene


class UsersQuery(graphene.ObjectType):
    users = graphene.List(UserType)

    def resolve_users(self, info):
        users = User.objects.all()
        users2 = []
        for user in users:
            if user.avatar:
                user.avatar.image = settings.MEDIA_HOST + user.avatar.image.name
            users2.append(user)
        return users2
