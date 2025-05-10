import flask
import zeeguu.core

api = flask.Blueprint("endpoints", __name__)
db_session = zeeguu.core.model.db.session

print("loading endpoints...")

# These files have to be imported after this line;
# They enrich the endpoints object
