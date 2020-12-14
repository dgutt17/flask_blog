from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand


app = Flask(__name__)
app.config['SQLAlCHEMY_DATABASE_URI'] = 'postgresql:///flask_blog_dev' 
db = SQLAlchemy(app)
migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)

class User(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(20), unique=True, nullable=False)
  email = db.Column(db.String(120), unique=True, nullable=False)
  image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
  password = db.Column(db.String(60), nullable=False)
  posts = db.relationship('Post', backref='author', lazy=True)

  def __repr__(self):
    return f"User('{self.username}', '{self.email}', '{self.image_file}')"

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    author = db.relationship('Author')

    def __repr__(self):
      return f"Post('{self.title}', '{self.date_posted}')"

posts = [
  {
    'author': 'Test',
    'title': 'Post 1',
    'content': 'First Content',
    'date_posted': 'April 20, 2020'
  },
  {
    'author': 'Test 2',
    'title': 'Post 2',
    'content': 'More fake content',
    'date_posted': 'November 3, 2020'
  }
]

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts)

@app.route('/about')
def about():
  return render_template('about.html', title='About')


# This only works if you start the server with python flask_blog.py
# Does not work if you just use flask run
if __name__ == '__main__':
  app.run(debug=True)