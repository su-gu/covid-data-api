from graphene import ObjectType, Schema
from covidApi.schema import Query as api_query
import graphene
class Query(api_query):
    pass

schema = Schema(query=Query)
