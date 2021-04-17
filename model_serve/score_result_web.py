import os
from flask import Flask, render_template, abort, url_for, json, jsonify
import json
import html

# Flask Web Server
app = Flask(__name__, template_folder='.')
app.config["DEBUG"] = True


@app.route('/')
def home():
    # Read json file
    with open('./score_result/result.json', 'r') as resultfile:
        data = resultfile.read()

    result = json.loads(data)
    gesture = str(result['gesture'])
    return render_template('./index.html', jsonfile=result, gesture=gesture)

app.run(port=5001)