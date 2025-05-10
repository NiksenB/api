import flask_sqlalchemy

db = flask_sqlalchemy.SQLAlchemy()


# If zeeguu.core.app is already defined we use that object
# as the app for the db_init that we do later. If not,
# we create the app here and load the corresponding configuration
# if not hasattr(zeeguu.core, "app"):
#     zeeguu.core.app = Flask("Zeeguu-Core")
#     load_configuration_or_abort(
#         zeeguu.core.app,
#         "ZEEGUU_CONFIG",
#         ["MAX_SESSION", "SQLALCHEMY_DATABASE_URI", "SQLALCHEMY_TRACK_MODIFICATIONS"],
#     )


# Create the zeeguu.core.db object, which will be the superclass
# of all the model classes
# zeeguu.core.db = flask_sqlalchemy.SQLAlchemy(zeeguu.core.app)
# Note, that if we pass the app here, then we don't need later
# to push the app context


# the core model







# exercises

# user logging

# teachers and cohorts



# New topic features



# bookmark scheduling



