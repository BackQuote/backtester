#!/usr/bin/env python
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS, cross_origin
import os

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
CORS(app)

from models import *

db = SQLAlchemy(app)

@app.route('/')
def api_root():
    return '<h1>BackQuote API</h1>'

@app.route('/algorithms')
def algorithms():
    algos = Algorithm.query.all()
    return jsonify([i.serialize for i in algos])

@app.route('/templates')
def templates():
    templates = Template.query.all()
    return jsonify([i.serialize for i in templates])

@app.route('/tickers')
def tickers():
    tickers = Ticker.query.all()
    return jsonify([i.serialize for i in tickers])

@app.route('/algorithms/<id>')
def algorithm(id):
    algorithm = Algorithm.query.get(id)
    return jsonify(algorithm.serialize)

@app.route('/results/<id>')
def result(id):
    result = Result.query.get(id)
    return jsonify(result.serialize)

@app.route('/days/<id>')
def day(id):
    day = Day.query.get(id)
    return jsonify(day.serialize)

@app.route('/trades/<id>')
def trade(id):
    trade = Trade.query.get(id)
    return jsonify(trade.serialize)

@app.route('/quotes/<id>')
def quote(id):
    quote = Quote.query.get(id)
    return jsonify(quote.serialize)

if __name__ == '__main__':
    app.run(debug=app.config['DEBUG'])