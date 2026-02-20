from flask import Flask, render_template,request,redirect,url_for
from flask import flash
from flask_wtf.csrf import CSRFProtect
from config import DevelopmentConfig
from flask import g
import forms
from models import db
from models import Alumnos

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
db.init_app(app)
csrf = CSRFProtect()

@app.route("/404")
def page_not_fount():
    return render_template("404.html"), 404

@app.route("/", methods=["GET","POST"])
@app.route("/index")
def index():
    create_form=forms.UserForm(request.form)
    
    alumnos=Alumnos.query.all()
    return render_template("index.html",form=create_form,alumnos=alumnos)

@app.route("/alumnos", methods=["GET","POST"])
def alumnos():
    create_from = forms.UserForm(request.form)

    if request.method == "POST" and create_from.validate():
        alum = Alumnos(
            nombre=create_from.nombre.data,
            apaterno=create_from.apaterno.data,
            email=create_from.email.data
        )

        db.session.add(alum)
        db.session.commit()

        return redirect(url_for("index"))

    return render_template("alumnos.html", form=create_from)


@app.route("/detalles",methods=["GET","POST"])
def detalles():
    if request.method=='GET':
        id = request.args.get('id')
        alum= db.session.query(Alumnos).filter(Alumnos.id==id).first()
        id = request.args.get('id')
        nombre = alum.nombre
        apaterno = alum.apaterno
        email = alum.email
    return render_template("detalles.html",nombre=nombre, apaterno = apaterno, email=email)
        
@app.route("/modificar",methods=["GET","POST"])
def modificar():
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
        alum= db.session.query(Alumnos).filter(Alumnos.id==id).first()
        alum.id = id
        alum.nombre = str-rstrip(create_form.nombre.data)
        alum.apaterno = create_form.aPaterno.data
        alum.email = create_form.email.data
    db.session.add(alum)
    db.session.commit()
    return render_template("detalles.html",nombre=create_form.nombre.data, apaterno = create_form.aPaterno.data, email=create_form.email.data)


    return render_template("alumnos.html", form=create_form)

if __name__ == '__main__':
    csrf = CSRFProtect(app)
    with app.app_context():
        db.create_all()
    app.run(debug=True)
