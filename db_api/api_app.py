from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

db.drop_all()


class ScanModel(db.Model):
    scan_id = db.Column(db.String, primary_key=True)
    domain = db.Column(db.String(100), nullable=False)
    insertion_time = db.Column(db.DATETIME, nullable=False)
    status = db.Column(db.String, nullable=False)


db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
