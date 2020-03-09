from flask import Flask, request, abort
app = Flask(__name__)

#flask run --host=0.0.0.0
@app.route("/status")
def status():
    # This could be a more complicated check to see if dependencies are online

    return("online")

@app.route("/evaluate", methods=["POST", "GET"])
def evaluate():
    # This should examine request.body to see if a request can be handled
    return("Allowed")


@app.route("/run", methods=["POST"])
def run():
    # This should return a result.

    return("")
