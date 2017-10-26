import sqlite3
import sqlalchemy

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import query


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///foo.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)


# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(80), unique=True, nullable=False)
#     email = db.Column(db.String(120), unique=True, nullable=False)
#
#     def __repr__(self):
#         return '<User %r>' % self.username


def tmprep(self):
    # print 'pass'
    print self.name
    pass


def makecls(cname):

    dict = {}

    dict['id'] = eval(makecol(0))
    dict['name'] = eval(makecol(1))

    cls = type(cname, (db.Model,), dict)

    return cls


def makecol(tp):
    if tp == 0:
        return 'db.Column(db.Integer, primary_key=True)'
    else:
        return 'db.Column(db.String(80), unique=True, nullable=False)'


# if __name__ == '__main___':

# db.create_all()
# test = cls(name='test')

cls = makecls('test3')
# kws = {'name': 'test3'}
# test = cls(**kws)
# db.session.add(test)
# db.session.commit()


@app.route('/')
def index():

    c = cls.query.all()
    s = ''
    for vv in c:
        print dir(vv)
        s += getattr(vv, 'name')
    return s


app.run()
