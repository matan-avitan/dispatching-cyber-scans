from flask_restful import Resource


class Ingest(Resource):

    def get(self):
        return {"id": 5}
