import graphene
from ..Types.UserType import UserType
from ..Models.User import User


class CreateUser(graphene.Mutation):
    user = graphene.Field(UserType)

    class Arguments:
        username = graphene.String(required=True)
        password = graphene.String(required=True)
        email = graphene.String(required=True)

    def mutate(self, info, username, password, email):
        user = User(username=username,
                    email=email)
        user.set_password(password)
        user.save()

        return CreateUser(user=user)
