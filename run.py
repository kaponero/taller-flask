from flask import Flask, render_template, request, redirect, url_for
import secrets

from forms import SignupForm

app = Flask(__name__)
app.config['SECRET_KEY'] = secrets.token_hex(32)

alumnos = ['Maia', 'Ingrid', 'Carli']

@app.route('/')
def Hello_world():
    return 'Alumnos son {}' .format(len(alumnos))


@app.route('/admin/<int:id>/')
@app.route('/admin/')
def index(id=None):
    return 'El id es {}' .format(id)

@app.route('/index/')
def index2(user2):
    return render_template('index.html', user=user2)

@app.route('/base/')
def base():
    return render_template('base.html', alumno='Carli')

@app.route('/inicio/', methods=["GET", "POST"])
def inicio():
    formu = SignupForm()
    if formu.validate_on_submit():
        usuario = formu.user.data
        pasw = formu.psw.data
        return redirect(url_for('index', user= usuario))
    return render_template('inicio.html', form=formu)


