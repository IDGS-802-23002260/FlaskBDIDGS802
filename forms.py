from wtforms import Form, RadioField
from wtforms import StringField, IntegerField, PasswordField
from wtforms import EmailField
from wtforms import validators

class UserForm(Form):
    id = IntegerField('ID', [
        validators.DataRequired(message="El campo es requerido")
    ])
    nombre = StringField('Nombre Alumno', [
        validators.DataRequired(message="El campo es requerido"),
        validators.Length(min=3, max=10, message="Ingrese un nombre válido")
    ])
    apaterno = StringField('Apaterno', [  # <- Debe coincidir con lo que usas en Jinja
        validators.DataRequired(message="El campo es requerido"),
    ])
    email = EmailField('Email', [
        validators.DataRequired(message="El campo es requerido"),
        validators.Email(message="Ingrese un correo válido"),
    ])