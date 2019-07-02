from ..Types.AvatarType import AvatarType
from ..Models.Avatar import Avatar
import graphene


class AvatarQuery(graphene.ObjectType):
    avatars = graphene.List(AvatarType)

    def resolve_avatars(self, info):
        return Avatar.objects.all()
