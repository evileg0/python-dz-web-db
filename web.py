from flask import Flask, render_template, request
from db_actions import *
import re

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route("/list", methods=['GET'])
def list():
    result = get_t_list()
    return result

@app.route("/stocks", methods=['GET'])
def data_by_ticker():
    ticker = request.args.get('ticker')
    if not ticker:
        return "Error: Parameter 'ticker' is required.", 400
    limit_rows = request.args.get('limitrows')
    if limit_rows:
        if not re.match(r'^-?\d+$', limit_rows):
            return "Error: Parameter 'limitrows' must be integer.", 400
    else:
        limit_rows =100
    result = get_data_by_ticker(ticker,limit_rows)
    return result

if __name__ == '__main__':
    app.run(debug=True)