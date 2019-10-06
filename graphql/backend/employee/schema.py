import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField
from .models import Employee


class EmployeeNode(SQLAlchemyObjectType):
    class Meta:
        model = Employee
        interfaces = (relay.Node,)


class EmployeeConnection(relay.Connection):
    class Meta:
        node = EmployeeNode
