from flask import Flask, render_template
app = Flask(__name__)

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