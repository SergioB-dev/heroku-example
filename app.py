from flask import Flask, request, jsonify
import os

app = Flask(__name__)


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


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
