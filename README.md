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





