import graphene
import graphql_jwt
import Modules.Users.schema
import Modules.Stock.schema


class Query(Modules.Users.schema.Query, Modules.Stock.schema.Query, graphene.ObjectType):
    pass


class Mutation(Modules.Users.schema.Mutation, Modules.Stock.schema.Mutation, graphene.ObjectType):
    refresh_token = graphql_jwt.Refresh.Field()
    verify_token = graphql_jwt.Verify.Field()
    revoke_token = graphql_jwt.Revoke.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
