from flask import Flask, render_template,request,redirect,url_for
from flask import flash
from flask_wtf.csrf import CSRFProtect
from config import DevelopmentConfig
from flask import g
import forms
from flask_migrate import Migrate

# Registro de modulos
from maestros.routes import maestros_bp # Que se no se repitan carpetas

from models import db
from models import Alumnos

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
app.register_blueprint(maestros_bp) 
csrf = CSRFProtect()
db.init_app(app)
migrate = Migrate(app, db)

@app.route("/404")
def page_not_fount():
    return render_template("404.html"), 404

@app.route("/", methods=["GET","POST"])
@app.route("/index")
def index():
    create_form=forms.UserForm(request.form)
    
    alumnos=Alumnos.query.all()
    return render_template("index.html",form=create_form,alumnos=alumnos)

@app.route("/Alumnos",methods=["GET","POST"])
def alumnos():
    create_form=forms.UserForm(request.form)
    if request.method=='POST':
        alum = Alumnos(
            nombre = create_form.nombre.data,
            apellidos = create_form.apellidos.data,
            email = create_form.email.data,
            telefono = create_form.telefono.data
        )
        db.session.add(alum)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template("alumnos.html",form=create_form)


@app.route("/detalles")
def detalles():
    id = request.args.get("id")
    alum = Alumnos.query.get_or_404(id)
    return render_template("detalles.html", alum=alum)
        
@app.route("/modificar", methods=["GET", "POST"])
def modificar():
    form = forms.UserForm(request.form)

    if request.method == "GET":
        id = request.args.get("id")
        alum = Alumnos.query.get_or_404(id)
        form.id.data = alum.id
        form.nombre.data = alum.nombre
        form.apellidos.data = alum.apellidos
        form.email.data = alum.email
        form.telefono.data = alum.telefono

    if request.method == "POST" and form.validate():
        alum = Alumnos.query.get_or_404(form.id.data)
        alum.nombre = form.nombre.data.strip()
        alum.apellidos = form.apellidos.data.strip()
        alum.email = form.email.data.strip()
        alum.telefono = form.telefono.data.strip()
        db.session.commit()
        flash("Alumno modificado correctamente", "info")
        return redirect(url_for("index"))

    return render_template("modificar.html", form=form)

@app.route("/eliminar",methods=["GET","POST"])
def eliminar():
    create_form=forms.UserForm(request.form)
    if request.method=='GET':
        id = request.args.get('id')
        alum= db.session.query(Alumnos).filter(Alumnos.id==id).first()
        create_form.id.data=request.args.get('id')
        create_form.nombre.data=alum.nombre
        create_form.aPaterno.data=alum.apaterno
        create_form.email.data=alum.email
    if request.method=='POST':
        id = create_form.id.data
        alum= db.session.query(Alumnos).get(id)
        db.session.delete(alum)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template("eliminar.html",form=create_form)

if __name__ == '__main__':
    csrf = CSRFProtect(app)
    with app.app_context():
        db.create_all()
    app.run(debug=True)
