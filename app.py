from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello World!"

@app.route("/family")
def family():
    return "Hello family!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))