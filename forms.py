from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import data_required

class SignupForm(FlaskForm):



    user = StringField('Usuario', validators=[data_required()])
    psw = PasswordField('Contraseña', validators=[data_required()])
    submit = SubmitField('Login')