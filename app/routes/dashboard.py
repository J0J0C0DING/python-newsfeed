from flask import Blueprint, render_template, session, redirect

bp = Blueprint('dashboard', __name__, url_prefix='/dashboard')

@bp.route('/')
def dash():
  if session.get('loggedIn') is None:
    return redirect('/login')

  return render_template('dashboard.html', loggedIn=session.get('loggedIn'))

@bp.route('/edit/<id>')
def edit(id):
  if session.get('loggedIn') is None:
    return redirect('/login')

  return render_template('edit-post.html', loggedIn=session.get('loggedIn'))