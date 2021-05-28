import os

from flask import Flask

from flask_restful import Api
from flask_cors import CORS, cross_origin
import logging
import sys
# from models.hexapod.view import hexapod_blueprint
app = Flask(__name__)
app.secret_key = "Secret Key"
api = Api(app)
cors = CORS(app)

app.secret_key = os.urandom(24)
app.config['CORS_HEADERS'] = 'Content-Type'
# app.register_bluseprint(hexapod_blueprint, url_prefix="/hexapod")

if __name__ == "__main__":

    app.run(host="0.0.0.0", debug=True, port=5000, threaded=True)
