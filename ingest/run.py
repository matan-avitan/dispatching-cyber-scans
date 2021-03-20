from ingest.app import create_app
from ingest.app.conf import Conf
app = create_app()

if __name__ == '__main__':
    app.run(port=5000, debug=False, threaded=True, processes=Conf.NUMBER_OF_REQUEST_PARALLEL)
