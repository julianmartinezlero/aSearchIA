from flask import Flask, jsonify, request
import json
from flask_cors import CORS, cross_origin
from static.aStar import AStar
from static.Node import Utils

from flask_cors import CORS

app = Flask(__name__)
# app.config['SECRET_KEY'] = 'the quick brown fox jumps over the lazy   dog'
# app.config['CORS_HEADERS'] = 'Content-Type'

cors = CORS(app, resources={r"*": {"origins": "*"}})

@app.route("/usuario", methods=['GET'])
# @cross_origin(origin='*')
def helloWorld():
  return "Hello, cross-origin-world!"

@app.route("/aSearch", methods=['POST'])
def a_search():
    data = json.loads(request.data)
    datass = convertOnDic(data)
    search = AStar(datass, data['origin'].get('label'), data['destin'].get('label'))
    res = search.a_start_search()

    return jsonify(res)
    # return data

def convertOnDic(nodes):
    graph = dict()
    allnode = nodes['nodos']
    aristas = nodes['aristas']
    for i in allnode:
        node = dict()
        node['heuristic'] = i['heuristic']
        node['childs'] = dict()
        graph[i['label']] = node

    for i in aristas:
        point_a = i['pointA']
        point_b = i['pointB']
        value = i['value']
        graph[point_a['label']]['childs'][point_b['label']] = value
        graph[point_b['label']]['childs'][point_a['label']] = value

    return graph

if __name__ == '__main__':
    app.run()
