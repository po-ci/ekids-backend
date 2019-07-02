import graphene
from ..Types.GroupType import GroupType
from ..Types.UserType import UserType
from ..Models.User import Group
from graphql_jwt.decorators import login_required, permission_required


class UserGroup(graphene.Mutation):
    group = graphene.Field(GroupType)
    user = graphene.Field(UserType)

    class Arguments:
        user = graphene.String()
        name = graphene.String()

    @login_required
    def mutate(self, info, user, name):
        group = Group.objects.get(name=name)
        group.user_set.add(user)
        return UserGroup(group=group, user=user)
