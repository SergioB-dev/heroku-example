from flask import Flask, request, jsonify
import os

app = Flask(__name__, template_folder='templates')


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'

@app.route('/cats', methods=['GET'])
def get_cat():
    if request.method == 'GET':
        print(request.data)
        data = {
            'rudolph': 'reindeer'
        }
        return jsonify(data)



