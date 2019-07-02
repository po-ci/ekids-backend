import graphene
from graphene_django.filter import DjangoFilterConnectionField
from .Types.UserNode import UserNode
from .Queries.UsersQuery import UsersQuery
from .Queries.MeQuery import MeQuery
from .Queries.GroupQuery import GroupQuery
from .Queries.PermissionQuery import PermissionQuery
from .Mutations.CreateUserMutation import CreateUser
from .Mutations.RegisterUserMutation import RegisterUserMutation
from .Mutations.UpdateUserMutation import UpdateUserMutation
from .Mutations.CreateGroupMutation import CreateGroup
from .Mutations.UserGroupMutation import UserGroup
from .Mutations.RecoveryPasswordMutation import RecoveryPassword
from .Mutations.ChangePasswordMutation import ChangePassword
from .Mutations.PermissionGroupMutation import PermissionGroup
from .Mutations.ObtainJSONWebTokenMutation import ObtainJSONWebToken
from .Mutations.AvatarMutation import AvatarMutation
from .Queries.AvatarQuery import AvatarQuery
from .Nodes.AvatarNode import AvatarNode


class Query(UsersQuery, MeQuery, GroupQuery, PermissionQuery, AvatarQuery):
    user = DjangoFilterConnectionField(UserNode)
    avatarnode = DjangoFilterConnectionField(AvatarNode)


class Mutation(graphene.ObjectType):
    create_user = CreateUser.Field()
    create_group = CreateGroup.Field()
    user_group = UserGroup.Field()
    permission_group = PermissionGroup.Field()
    register_user = RegisterUserMutation.Field()
    token_auth = ObtainJSONWebToken.Field()
    recovery_password = RecoveryPassword.Field()
    update_user = UpdateUserMutation.Field()
    change_password = ChangePassword.Field()
    avatar = AvatarMutation.Field()
