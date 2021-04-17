import flask
from flask import request, jsonify
import json

app = flask.Flask(__name__)
app.config["DEBUG"] = True

with open('./score_result/result.json') as json_file:
    result_data = json.load(json_file)

@app.route('/api/result', methods=['GET'])
def api_all():
    return jsonify(result_data)

app.run(port=5001)