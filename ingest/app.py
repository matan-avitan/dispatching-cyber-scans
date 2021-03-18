from flask import Flask
from flask_restful import Api
from ingest.resources.ingest import Ingest
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)
# db.create_all()

api.add_resource(Ingest, "/ingest")

if __name__ == '__main__':
    app.run(debug=True)
