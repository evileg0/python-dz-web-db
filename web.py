from flask import Flask, render_template, request
from db_actions import *

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
    result = get_data_by_ticker(ticker)
    return result

if __name__ == '__main__':
    app.run(debug=True)