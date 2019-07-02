import graphene
from graphene_file_upload.scalars import Upload

from stockApi import settings
from ..Models.Avatar import Avatar
from ..Models.User import User, Group
from ..Types.UserType import UserType
from graphql_jwt.decorators import login_required, permission_required
from graphene_django.forms.mutation import DjangoModelFormMutation
from ..Forms.AvatarForm import AvatarForm


class AvatarMutation(graphene.Mutation):
    class Arguments:
        id = graphene.Int()
        avatar = Upload(required=True)

    ok = graphene.Boolean()
    id = graphene.Int()
    image = graphene.String()

    @login_required
    def mutate(self, info, id, avatar):

        user = User.objects.get(id=id)

        if user.avatar:
            user.avatar.image = avatar
            user.avatar.save()
        else:

            avataruser = Avatar(image=avatar)
            avataruser.save()
            user.avatar = avataruser
            user.avatar.save()

        user.save()
        newavatar = settings.MEDIA_HOST + user.avatar.image.name
        return AvatarMutation(ok=True, id=id, image=newavatar)
