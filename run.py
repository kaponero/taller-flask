from flask import Flask, render_template

app = Flask(__name__)

alumnos = ['Maia', 'Ingrid', 'Carli']

@app.route('/')
def Hello_world():
    return 'Alumnos son {}' .format(len(alumnos))


@app.route('/admin/<int:id>/')
@app.route('/admin/')
def index(id=None):
    return 'El id es {}' .format(id)

@app.route('/index/')
def index2():
    return render_template('index.html')

@app.route('/base/')
def base():
    return render_template('base.html', alumno='Carli')

@app.route('/inicio/')
def inicio():
    return render_template('inicio.html')


