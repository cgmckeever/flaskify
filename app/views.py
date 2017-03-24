from IPython import embed
from flask import render_template, flash, redirect, request
from app import app
from .forms import LoginForm

@app.route('/')
@app.route('/index')

def index():
  user = {'nickname': 'Miguel'}  # fake user
  posts = [  # fake array of posts
      {
          'author': {'nickname': 'John'},
          'body': 'Beautiful day in Portland!'
      },
      {
          'author': {'nickname': 'Susan'},
          'body': 'The Avengers movie was so cool!'
      }
  ]
  return render_template("index.html",
                         title='Home',
                         user=user,
                         posts=posts)


@app.route('/login', methods=['GET', 'POST'])

def login():
  embed()
  form = LoginForm(request.form)
  if request.method == 'POST' and not form.validate():
    flash('Login requested for OpenID="%s", remember_me=%s' %
          (form.openid.data, str(form.remember_me.data)))
    embed()
    return redirect('/index')
  return render_template('login.html',
                          title='Sign In',
                          form=form)
