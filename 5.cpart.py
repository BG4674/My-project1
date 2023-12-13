from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class User(db.Model):
    id, username, email = db.Column(db.Integer, primary_key=True), db.Column(db.String(255), nullable=False), db.Column(db.String(255), nullable=False)

class ToDoList(db.Model):
    id, user_id, name, user = db.Column(db.Integer, primary_key=True), db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False), db.Column(db.String(255), nullable=False), db.relationship('User', backref=db.backref('todolists', lazy=True))

class Task(db.Model):
    id, list_id, name, description, due_date, is_completed, todolist = db.Column(db.Integer, primary_key=True), db.Column(db.Integer, db.ForeignKey('to_do_list.id'), nullable=False), db.Column(db.String(255), nullable=False), db.Column(db.Text), db.Column(db.Date), db.Column(db.Boolean, default=False), db.relationship('ToDoList', backref=db.backref('tasks', lazy=True))

@app.route('/')
def index(): return render_template('index.html', users=User.query.all())

if __name__ == '__main__':
    db.create_all(), app.run(debug=True)
