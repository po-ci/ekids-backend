import graphene
from ..Types.UserType import UserType
from ..Models.User import User, Group
from graphql import GraphQLError
from graphql_jwt.decorators import login_required, permission_required
from graphene_django.forms.mutation import DjangoModelFormMutation
from ..Forms.UserForm import UserForm


class RegisterUserMutation(DjangoModelFormMutation):
    user = graphene.Field(UserType)

    class Meta:
        form_class = UserForm

