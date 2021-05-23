import flask
from flask import request,jsonify


app = flask.Flask(__name__)

# @app.route("/api",method=["POST"])
@app.route("/",methods=["GET"])
def response():
    try:
        #query = dict(request.form)["query"]
        #return jsonify({"response" : query})
        return jsonify({"response" : 'hi this is python'})
    error:
        return jsonify({"response" : 'hi this is python'})

