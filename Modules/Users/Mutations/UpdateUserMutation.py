import graphene
from ..Models.User import User, Group
from ..Types.UserType import UserType
from graphql_jwt.decorators import login_required, permission_required
from graphene_django.forms.mutation import DjangoModelFormMutation
from ..Forms.UserForm import UpdateUserForm


class UpdateUserMutation(DjangoModelFormMutation):
    user = graphene.Field(UserType)

    class Meta:
        form_class = UpdateUserForm



