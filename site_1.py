from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p color='red'><h1><u>I Love Lilli the most! and more! and always will</u></h1></p>"