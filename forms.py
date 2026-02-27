from flask_wtf import FlaskForm
from wtforms import StringField, HiddenField
from wtforms import EmailField
from wtforms import validators

class UserForm(FlaskForm):
    id = HiddenField()

    nombre = StringField('Nombre Alumno', [
        validators.DataRequired(message="El campo es requerido"),
        validators.Length(min=3, max=50, message="Ingrese un nombre válido")
    ])

    apellidos = StringField('Apellidos', [
        validators.DataRequired(message="El campo es requerido"),
        validators.Length(min=3, max=200, message="Ingrese apellidos válidos")
    ])

    email = EmailField('Email', [
        validators.DataRequired(message="El campo es requerido"),
        validators.Email(message="Ingrese un correo válido"),
    ])

    telefono = StringField('Teléfono', [
        validators.Length(min=7, max=20, message="Ingrese un teléfono válido")
    ])
    


class MaestroForm(FlaskForm):
    id = HiddenField()

    matricula = StringField('Matrícula', [
        validators.DataRequired(message="La matrícula es requerida"),
        validators.Length(min=3, max=50, message="Ingrese una matrícula válida")
    ])

    nombre = StringField('Nombre', [
        validators.DataRequired(message="El nombre es requerido"),
        validators.Length(min=3, max=200, message="Ingrese un nombre válido")
    ])

    apellidos = StringField('Apellidos', [
        validators.DataRequired(message="Los apellidos son requeridos"),
        validators.Length(min=3, max=120, message="Ingrese apellidos válidos")
    ])

    especialidad = StringField('Especialidad', [
        validators.DataRequired(message="La especialidad es requerida"),
        validators.Length(min=3, max=20, message="Ingrese una especialidad válida")
    ])

    email = EmailField('Correo electrónico', [
        validators.DataRequired(message="El correo es requerido"),
        validators.Email(message="Ingrese un correo válido"),
    ])