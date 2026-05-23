from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///schools.db'

db = SQLAlchemy(app)


class School(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))


@app.route('/')
def home():

    schools = School.query.all()

    text = ""

    for school in schools:
        text += f"{school.name}<br>"

    return text


@app.route('/add/<name>')
def add(name):

    school = School(name=name)

    db.session.add(school)
    db.session.commit()

    return "School Added"


if __name__ == '__main__':

    with app.app_context():
        db.create_all()

    app.run(debug=True)
