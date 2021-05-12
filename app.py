from flask import Flask,request,jsonify
from flask_cors import CORS


app = Flask(__name__)
CORS(app=app)

@app.route('/api',methods=['GET'])

def hello_world():
    d={}
    d['Query'] = str(request.args['Query'])
    return jsonify(d)


if __name__ == '__main__':
    app.run(host="0.0.0.0",)
    