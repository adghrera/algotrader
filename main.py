from ariadne import QueryType, graphql_sync, make_executable_schema
from ariadne.constants import PLAYGROUND_HTML
from flask import Flask, request, jsonify
from ariadne import load_schema_from_path
# from ariadne.asgi import GraphQL

# Load schema from file...
# type_defs = load_schema_from_path("/path/to/schema.graphql")

# ...or construct schema from all *.graphql files in directory
from resolvers.scalars import get_scalars
from resolvers.setup_resolvers import setup
# from dbsetup import setup as setup_db

type_defs = load_schema_from_path("myschema")


# Build an executable schema
schema = make_executable_schema(type_defs)


# type_defs = """
#     type Query {
#         hello: String!
#     }
# """

query = QueryType()
setup(query)


# @query.field("hello")
# def resolve_hello(_, info):
#     request = info.context
#     user_agent = request.headers.get("User-Agent", "Guest")
#     return "Hello, %s!" % user_agent


scalars = get_scalars()
resolvers = [query]
resolvers.extend(scalars)

schema = make_executable_schema(type_defs, query, scalars)
app = Flask(__name__)
# db = None
# setup_db()
import dbsetup

@app.route("/graphql", methods=["GET"])
def graphql_playgroud():
    # On GET request serve GraphQL Playground
    # You don't need to provide Playground if you don't want to
    # but keep on mind this will not prohibit clients from
    # exploring your API using desktop GraphQL Playground app.
    return PLAYGROUND_HTML, 200


@app.route("/graphql", methods=["POST"])
def graphql_server():
    # GraphQL queries are always sent as POST
    data = request.get_json()

    # Note: Passing the request to the context is optional.
    # In Flask, the current request is always accessible as flask.request
    success, result = graphql_sync(
        schema,
        data,
        context_value=request,
        debug=app.debug
    )

    status_code = 200 if success else 400
    return jsonify(result), status_code


if __name__ == "__main__":
    app.run(debug=True)