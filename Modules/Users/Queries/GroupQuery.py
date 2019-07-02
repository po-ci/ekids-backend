from ..Types.GroupType import GroupType
from ..Models.User import Group
import graphene


class GroupQuery(graphene.ObjectType):
    group = graphene.Field(graphene.List(GroupType))

    def resolve_group(self, info):
        return Group.objects.all()
