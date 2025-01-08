from flask import Flask
from src.logger import logging

app = Flask(__name__)

@app.route('/', methods = ['GET','POST'])

def index():
    logging.info("testing second methond of logging")
    return "Welcome to the ML pipeline Project"

if __name__ =="__main__":
    app.run(debug=True)