from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p><div style='background-color:maroon'><h1 color='red'><u>I Love Lilli the most! and more! and always will and every day!</u></h1></div></p>"