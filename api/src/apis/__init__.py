from flask import Blueprint
from flask_restx import Api

from src.apis.bots import bots_ns
# from src.apis.status import status_ns

api_v1_db = Blueprint('api_v1', __name__)
api = Api(
    api_v1_db,
    title='Flask API for TMSell',
    version='0.1',
    description='Welcome to the Swagger UI documentation site!'
)

api.add_namespace(bots_ns)
# api.add_namespace(status_ns)