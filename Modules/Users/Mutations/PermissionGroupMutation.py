import graphene
from ..Types.GroupType import GroupType
from ..Types.PermissionType import PermissionType
from ..Models.User import Group
from graphql_jwt.decorators import login_required, permission_required


class PermissionGroup(graphene.Mutation):
    group = graphene.Field(GroupType)
    permission = graphene.Field(PermissionType)

    class Arguments:
        permission = graphene.String()
        name = graphene.String()

    @login_required
    def mutate(self, info, permission, name):
        group = Group.objects.get(name=name)
        group.permissions.add(permission)
        return PermissionGroup(group=group)
