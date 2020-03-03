from flask import render_template
from app import app
from app.forms import LoginForm

@app.route('/login', methods=['GET', 'POST'])
def login():
  form = LoginForm()
  return render_template('login.html', title='Sign In', form=form)

@app.route('/index')
@app.route('/')
def index():
  user = {'username': 'Reggie'}
  posts = [
    {
      'author': {'username': 'John'},
      'body': 'Beautiful day in Portland!'
      },
      {
        'author': {'username': 'Susan'},
        'body': 'The Avengers movie was so cool!'
      }
      ]
  return render_template('index.html', title='Home', user=user, posts=posts)
