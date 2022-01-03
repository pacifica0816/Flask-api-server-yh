from flask import Flask, request
from flask import jsonify
from http import HTTPStatus

from werkzeug.wrappers import request

from flask_restful import Api

app = Flask(__name__)

api = Api(app)

# 경로와 리소스를 연결한다.



if __name__ == "__main__" :
    app.run()