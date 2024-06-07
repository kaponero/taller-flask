# Taller Flask
## 1 - Introducción
### Crear directorio de proyecto
    mkdir myproject
    cd myproject
    python3 -m venv .venv
### en Windows
    mkdir myproject
    cd myproject
    py -3 -m venv .venv
### Activar entorno
    source .venv/bin/activate
### Desactivar entorno
    deactivate
### instalar Flask
    pip install Flask
## 2 - Hellow World
### Crear fichero run.py
    from flask import Flask
    app = Flask (__name__)

    @app.route('/')
    def hello_world():
      return 'Hello World'

  Toda aplicación flask es una instancia de la clase flask, por lo que importamos la clase y creamos una instancia en este caso llamada app. Al crear esta instancia debemos pasarle el nombre del módulo como argumento.
## 3 - Lanzando el servidor Flask
### Variables de entorno en .venv
    $pip install python-dotenv
### Crear el archivo .flaskenv
    FLASK_APP = run.py
    FlASK_DEBUG = 1
    FLASK_RUN_PORT = 6000
### Lanzar el servidor
    flask run
## 4 - Enrutamiento y plantillas
### Enrutamiento
    pacientes = [ ]
 
    @app.route('/pacientes/')
    Def lista_pacientes( ):
 		  return '{} pacientes' .format(len(pacientes))
 
    /* Se creo una variable pacientes  y en la función lista_pacientes( ) muestra en el navegador el numero de pacientes*/
### Web dinámica
    @app.route('p/<string:name>/')
    Def mostrar_paciente(name):
 		  return 'Mostrando al paciente { }' .format(name)
  A una URL se le puede añadir secciones parametrizadas con <parámetro> y  opcionalmente agregar un conversor para especificar el tipo de dato
### Múltiples enrutamientos a URL única
    @app.route('/admin/paciente/')
    @app.route('/admin/paciente/<int:id>/')
    def agregar_paciente(id=None):
 		  return 'Paciente {}' .format(id)
  Crear dos endpoints a una url utilizando dos decoradores a la vez
### Render a una plantilla HTML
    render_template('index.html', param='name')
  Flask busca por defecto las plantillas en el directorio templates. 
### Antes debemos importar el método render_template
    From flask import render_template
### Archivos estaticos
    Estilos (css)
    Javascript (js)
    Imágenes (img)
  Ubicar estos archivos en una carpeta llamada static en el mismo nivel que el directorio templates
    Usar la función url_for('static', filename=base.css )
## 5 - Enviar parámetros
### Enviar parámetros al template
    return render_template ("index.html", usuarios=8)
### Código jinja2 para leer los parámetros usados {{}}
    <h3> Cantidad de Usuarios {{usuarios}} </h3>
### Estructuras de control {%%}
    {% if usuarios >10 %}
      <h3>Cantidad de Usuarios {{usuarios}}</h3>
    {% else %}
    	<h3>Pocos usuarios</h3>
    {% endif %}
## 6 - Herencia
### Agregar bloques de herencia en la estructura html
    {% block title %}
      {% endblock %}

    {% block links %}
      {% endblock %}

    {% block body %}
      {% endblock %}

    {% block javascripts %}
        {% endblock javascripts %}
### Método de herencia
     {% extends "base.html" %}
  Al principio del fichero html hijo
## 7 - Formularios
### Acceder a los datos de una petision GET en Flask
    from flask import request
    @app.route("/")
    def index():
        usuario = request.args.get('user')
        contraseña = request.args.get('psw')
### Methods POST
    @app.route("/", methods=["GET", "POST"])
### Petision POST
    from flask import render_template, request, redirect, url_for

    @app.route("/inicio/", methods=["GET", "POST"])
    def inicio():
    if request.method == 'POST':
        user = request.form['user']
        password = request.form['psw']

        return redirect(url_for('inicio'))
    return render_template("inicio.html")
## Formularios con Flask-WTF
### Instalar Flask-WTF
    pip install Flask-WTF
    pip install email-validator
### Formulario usando Flask-WTF en forms.py
    from flask_wtf import FlaskForm
    from wtforms import StringField, SubmitField, PasswordField
    from wtforms.validators import DataRequired

    class SignupForm(FlaskForm):
        user = StringField('Usuario', validators=[DataRequired()])
        password = PasswordField('Password', validators=[DataRequired()])
        submit = SubmitField('Login')
### Plantilla para el formulario
    <form action="" method="post" novalidate>
        {{ form.hidden_tag() }}
        <div>
            {{ form.user.label }}
            {{ form.user }}
            {% for error in form.name.errors %}
            <span style="color: red;">{{ error }}</span>
            {% endfor %}
        </div>
        <div>
            {{ form.password.label }}
            {{ form.password }}<br>
            {% for error in form.password.errors %}
            <span style="color: red;">{{ error }}</span>
            {% endfor %}
        </div>
        <div>
            {{ form.submit() }}
        </div>
    </form>
### Procesar el formulario
    from forms import SignupForm

    @app.route("/inicio/", methods=["GET", "POST"])
    def inicio():
        form = SignupForm()
        if form.validate_on_submit():
            user = form.user.data
            password = form.password.data

        return redirect(url_for('inicio'))
    return render_template("inicio.html", form=form)
### Configurar token contra ataques CSRF
    import secrets

    app = Flask( __name__)
    app.config['SECRET_KEY'] = secrets.token_hex(32)


