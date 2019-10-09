from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
from static.aStar import AStar

from flask_cors import CORS

app = Flask(__name__)
# app.config['SECRET_KEY'] = 'the quick brown fox jumps over the lazy   dog'
# app.config['CORS_HEADERS'] = 'Content-Type'

cors = CORS(app, resources={r"*": {"origins": "*"}})

@app.route("/usuario", methods=['GET'])
# @cross_origin(origin='*')
def helloWorld():
  return "Hello, cross-origin-world!"


if __name__ == '__main__':
    app.run()
