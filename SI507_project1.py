from flask import Flask
from lab3_code import *

app = Flask(__name__)

@app.route('/')
def home():
    return 'Welcome to Project1 Currency home page.'
