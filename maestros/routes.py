from flask import Flask, render_template,request,redirect,url_for
from flask import flash
from flask_wtf.csrf import CSRFProtect
from config import DevelopmentConfig
from flask import g
import forms
from flask_migrate import Migrate
from flask import Blueprint
import forms
from forms import MaestroForm

from models import db
from models import Maestros

maestros_bp=Blueprint('maestros',__name__)

@maestros_bp.route("/maestros", methods=["GET", "POST"])
def maestros():
    create_form = forms.MaestroForm(request.form)
    maestros = Maestros.query.all()
    return render_template("maestros.html",form=create_form,maestros=maestros)

@maestros_bp.route("/maestros/agregar", methods=["GET", "POST"])
def agregar_maestro():

    form = MaestroForm(request.form)

    if request.method == "POST" and form.validate():

        maestro = Maestros(
            matricula=form.matricula.data,
            nombre=form.nombre.data,
            apellidos=form.apellidos.data,
            especialidad=form.especialidad.data,
            email=form.email.data
        )

        db.session.add(maestro)
        db.session.commit()

        return redirect(url_for("maestros.maestros"))  

    return render_template("agregar_maestro.html", form=form)

@maestros_bp.route("/detalles")
def detalles_maestro():
    id = request.args.get("id")
    maestro = Maestros.query.get_or_404(id)
    return render_template("detalles_maestro.html", maestro=maestro)

@maestros_bp.route("/modificar", methods=["GET", "POST"])
def modificar_maestro():
    form = MaestroForm(request.form)

    if request.method == "GET":
        id = request.args.get("id")
        maestro = Maestros.query.get_or_404(id)

        form.id.data = maestro.id
        form.matricula.data = maestro.matricula
        form.nombre.data = maestro.nombre
        form.apellidos.data = maestro.apellidos
        form.especialidad.data = maestro.especialidad
        form.email.data = maestro.email

    if request.method == "POST" and form.validate():
        maestro = Maestros.query.get_or_404(form.id.data)

        maestro.matricula = form.matricula.data.strip()
        maestro.nombre = form.nombre.data.strip()
        maestro.apellidos = form.apellidos.data.strip()
        maestro.especialidad = form.especialidad.data.strip()
        maestro.email = form.email.data.strip()

        db.session.commit()
        return redirect(url_for("maestros.maestros"))  
        # Cambia a listar_maestros si así se llama tu función

    return render_template("modificar_maestro.html", form=form)

@maestros_bp.route("/eliminar", methods=["GET", "POST"])
def eliminar_maestro():
    form = MaestroForm(request.form)

    if request.method == "GET":
        id = request.args.get("id")
        maestro = Maestros.query.get_or_404(id)

        form.id.data = maestro.id
        form.matricula.data = maestro.matricula
        form.nombre.data = maestro.nombre
        form.apellidos.data = maestro.apellidos
        form.especialidad.data = maestro.especialidad
        form.email.data = maestro.email

    if request.method == "POST":
        maestro = Maestros.query.get_or_404(form.id.data)
        db.session.delete(maestro)
        db.session.commit()

        return redirect(url_for("maestros.maestros"))
        # cambia si tu listar se llama diferente

    return render_template("eliminar_maestro.html", form=form)