from graphene_django import DjangoObjectType
import graphene
from abcd.models import Todo




class User(DjangoObjectType):
    class Meta:
        model = Todo

class Query(graphene.ObjectType):
    users = graphene.List(User)

    def resolve_users(self, info):
        return Todo.objects.all()

schema = graphene.Schema(query=Query)