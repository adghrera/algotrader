# from flask import Flask, request, flash, url_for, redirect, render_template
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import types, UniqueConstraint, Index, ForeignKey

# from main import app, db

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.sqlite3'
# app.config['SECRET_KEY'] = "random string"
# app.config['SECRET_KEY'] = "random string"
db_uri = 'mysql+pymysql://demo:demo@localhost/demo'
app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Symbols(db.Model):
    id = db.Column(types.Integer, primary_key=True)
    name = db.Column(types.String(100))
    symbol = db.Column(types.String(10), unique=True, index=True)
    industry = db.Column(types.String(50))
    start_date = db.Column(types.Date)
    end_date = db.Column(types.Date)

    def __init__(self, name, symbol, industry):
        self.name = name
        self.symbol = symbol
        self.industry = industry
        self.start_date = None
        self.end_date = None


class Prices(db.Model):
    id = db.Column(types.Integer, primary_key=True)
    symbol_id = db.Column(types.Integer, ForeignKey('symbols.id'), index=True)
    date = db.Column(types.Date, index=True)
    open = db.Column(types.Float)
    close = db.Column(types.Float)
    high = db.Column(types.Float)
    low = db.Column(types.Float)

    __table_args__ = (
        # UniqueConstraint('symbol_id', 'date'),
        Index('ix_prices_symbol_date', 'symbol_id', 'date', unique=True),
    )

    def __init__(self, symbol_id, date, _open, close, high, low):
        self.symbol_id = symbol_id
        self.date = date
        self.open = _open
        self.close = close
        self.high = high
        self.low = low


def setup():
    global db
    db_uri = 'mysql+pymysql://demo:demo@localhost/demo'
    app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    db = SQLAlchemy(app)
    db.create_all()


db.drop_all()
db.create_all()
