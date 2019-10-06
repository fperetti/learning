import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField
from .models import Department


class DepartmentNode(SQLAlchemyObjectType):
    class Meta:
        model = Department
        interfaces = (relay.Node,)


class DepartmentConnection(relay.Connection):
    class Meta:
        node = DepartmentNode

