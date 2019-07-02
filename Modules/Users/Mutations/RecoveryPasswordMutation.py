from graphql_jwt.decorators import login_required, permission_required
import graphene
from ..Types.MailType import MailType
from ..Controller.RecoveryController import recovery
from stockApi.settings import SENDER_MAIL
import datetime
from ..Models.Mail import Mail
import pytz


class RecoveryPassword(graphene.Mutation):
    mail = graphene.Field(MailType)

    class Arguments:
        to = graphene.String()

    def mutate(self, info, to):
        print(to)
        recovery("Recuperar Contraseña", to)
        date = datetime.datetime.now(pytz.timezone('America/Argentina/Buenos_Aires'))
        getMail = Mail.objects.create(sender=SENDER_MAIL, to=to, message="Mail para recuperar contraseña",
                                      subject="Recuperar Contraseña",
                                      date=date)
        return RecoveryPassword(mail=getMail)
