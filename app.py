from flask import Flask,request,jsonify


app = Flask(__name__)

# @app.route("/api",method=["POST"])
@app.route("/",methods=["GET"])
def response():
    #query = dict(request.form)["query"]
    #return jsonify({"response" : query})
    return jsonify({"response" : 'hi this is python'})


if __name__ == "__main__":
    app.run(debug=True)
    