import uuid
from flask_restful import Resource


class Ingest(Resource):

    def get(self):
        return {"scan-id": str(uuid.uuid4())}
