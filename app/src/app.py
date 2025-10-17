from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import os
import time

app = Flask(__name__, template_folder='../templates', static_folder='../static')

# Database configuration
MYSQL_HOST = os.getenv('MYSQL_HOST', 'mysql')
MYSQL_USER = os.getenv('MYSQL_USER', 'flaskuser')
MYSQL_PASSWORD = os.getenv('MYSQL_PASSWORD', 'flaskpass')
MYSQL_DB = os.getenv('MYSQL_DB', 'mydb')

app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}/{MYSQL_DB}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Database Model
class Todo(db.Model):
    __tablename__ = 'todos'
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    completed = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f'<Todo {self.id}: {self.content}>'

# Wait for MySQL to be ready
def wait_for_db():
    retries = 5
    while retries > 0:
        try:
            db.create_all()
            print("Database connected successfully!")
            return
        except Exception as e:
            print(f"Database connection failed: {e}. Retrying in 5 seconds...")
            time.sleep(5)
            retries -= 1
    print("Could not connect to database after multiple attempts.")

# Routes
@app.route('/')
def index():
    todos = Todo.query.all()
    return render_template('index.html', todos=todos)

@app.route('/add', methods=['POST'])
def add_todo():
    content = request.form.get('content')
    if content:
        new_todo = Todo(content=content)
        db.session.add(new_todo)
        db.session.commit()
    return redirect(url_for('index'))

@app.route('/complete/<int:id>')
def complete_todo(id):
    todo = Todo.query.get_or_404(id)
    todo.completed = not todo.completed
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/delete/<int:id>')
def delete_todo(id):
    todo = Todo.query.get_or_404(id)
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/health')
def health():
    return {'status': 'healthy', 'service': 'flask-todo-app'}, 200

if __name__ == '__main__':
    with app.app_context():
        wait_for_db()
    app.run(host='0.0.0.0', port=5000, debug=False)
