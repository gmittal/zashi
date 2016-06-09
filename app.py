from flask import Flask
import numpy as np
app = Flask(__name__)

def sigmoid(score):
    return 1/(1+np.exp(-score))

@app.route("/", methods=["GET"])
def hello():
    return "Hello World!"

@app.route("/read", methods=["POST"])
def read():
    return "Something"

if __name__ == "__main__":
    print sigmoid(-0.5)
    app.run()
