from flask import Flask
from flask_restful import Api
from ingest.resources.ingest import Ingest

app = Flask(__name__)
api = Api(app)

api.add_resource(Ingest, "/ingest")

if __name__ == '__main__':
    app.run()
