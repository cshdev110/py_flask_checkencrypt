from flask import Flask, render_template
#from app import app

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')