import graphene
from covidApi.views import getStateWiseReport
from graphene import JSONString, Field
class Query(graphene.ObjectType):
    state_wise_data = graphene.JSONString()

    def resolve_state_wise_data(self, info, **kwargs):
        return getStateWiseReport()



# class StateWiseData(graphene.ObjectType):
#     data = Field(JSONString