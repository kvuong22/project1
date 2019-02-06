from flask import Flask
from lab3_code import *

app = Flask(__name__)

@app.route('/')
def home():
    return 'Welcome to the banking application!'

# print("Testing")

@app.route('/bank/<name>')
def bank(name):
    bank_name = Bank(name,Dollar)
    return 'Welcome to {}!'.format(bank_name.name)

@app.route('/dollar/<amt>')
def dollar(amt):
    d = Dollar(int(amt))
    return d.__str__()

@app.route('/yuan/<amt>')
def yuan(amt):
    y = Yuan(int(amt))
    return y.__str__()

@app.route('/pound/<amt>')
def pound(amt):
    p = Pound(int(amt))
    return p.__str__()

@app.route('/bank/<name>/<currency>/<value>')
def bank_currency_amt_text(name,currency,value):
    if currency == "Dollar":
        currency = Dollar
    elif currency == "Pound":
        currency = Pound
    elif currency =="Yuan":
        currency = Yuan
    else:
        return "INVALID URL inputs for bank."
    b = Bank(name,currency,int(value))
    return b.__str__()


if __name__ == '__main__':
    app.run()
