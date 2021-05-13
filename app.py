from flask import Flask,request,jsonify


app = Flask(__name__)

@app.route("/api",method=["POST"])

def response():
    query = dict(request.form)["query"]
    return jsonify({"response" : query})


if __name__ == "s__main__":
    app.run(host="0.0.0.0",)
    