from flask import Flask
from flask_cors import CORS
from flask_graphql import GraphQLView

from db import db_session
from schemas import schema

app = Flask(__name__)
CORS(app)
app.debug = True

app.add_url_rule(
    '/graphql',
    view_func=GraphQLView.as_view(
        'graphql',
        schema=schema,
        graphiql=True # for having the GraphiQL interface
    )
)

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()

if __name__ == '__main__':
    app.run()
