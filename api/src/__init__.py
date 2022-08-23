from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from elasticapm.contrib.flask import ElasticAPM
from elasticsearch import Elasticsearch

db = SQLAlchemy()
app = Flask(__name__)
es_host = "http://elasticsearch:9200"
print('Elastic host is {}'.format(es_host))
es = Elasticsearch([es_host])
def create_app():
    from src.apis import api_v1_db

    app.config['ELASTIC_APM'] = {
        'SERVICE_NAME': 'test-flask',
        'DEBUG': True
    }
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql+psycopg2://postgres:postgres@tmsell_db_1:5432/postgres'
    db.init_app(app)
    migrate = Migrate(app, db)
    app.register_blueprint(api_v1_db, url_prefix="/api/v1")
    # from .models import model_bots
    # app.config['MONGODB_SETTINGS'] = {
    #     "db": 'jobs-dag',
    #     "host": 'mongodb',
    #     "port": 27017,
    #     "username": 'root',
    #     "password": 'example'
    # }

    # db.init_app(app)
    return app
