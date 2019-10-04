import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField


from employee.schema import EmployeeConnection
from department.schema import DepartmentConnection


class Query(graphene.ObjectType):
    node = relay.Node.Field()

    # Add all schemas
    all_employees = SQLAlchemyConnectionField(EmployeeConnection)
    all_departments = SQLAlchemyConnectionField(DepartmentConnection, sort=None)


schema = graphene.Schema(query=Query)