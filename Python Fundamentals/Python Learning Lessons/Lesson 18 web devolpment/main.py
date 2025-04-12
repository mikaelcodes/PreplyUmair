from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

# Set the path for the SQLite database
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    complete = db.Column(db.Boolean)

@app.route('/fruits')
def main2():
    fruits = ['apple', 'orange', 'mango', 'strawberry', 'mikael']
    links = [
        'https://i5.walmartimages.ca/images/Enlarge/094/514/6000200094514.jpg',
        'https://i5.walmartimages.ca/images/Enlarge/234/6_r/6000191272346_R.jpg?odnHeight=2000&odnWidth=2000&odnBg=FFFFFF',
        'https://assets.shop.loblaws.ca/products/20121509001/b2/en/front/20121509001_front_a06_@2.png',
        'https://c02.purpledshub.com/uploads/sites/41/2023/09/GettyImages_154514873.jpg?w=1029&webp=1',
        'MIKAEL',
    ]
    together = zip(fruits, links)
    return render_template('fruits.html', mikael=together)

@app.route('/todo')
def main3():
    tasks = ['Buy fruits', 'Clean house', 'Cook dinner', 'Read book', 'Mikael']
    completed_tasks = Todo.query.filter_by(complete=True).all()
    incomplete_tasks = Todo.query.filter_by(complete=False).all()
    return render_template('todo.html', tasks=tasks, completed_tasks=completed_tasks, incomplete_tasks=incomplete_tasks)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
