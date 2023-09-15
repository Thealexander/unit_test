from flask import Blueprint, render_template, request, jsonify
from models.user import User
from utils.db import db

usuario = Blueprint('usuario', __name__)


@usuario.route('/', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        nombre = request.form["nombre"]
        ciudad = request.form["ciudad"]
        correo = request.form["correo"]
        nuevo_usuario = User(nombre, correo, ciudad)
        db.session.add(nuevo_usuario)
        db.session.commit()
        return render_template('index.html')
        # pass
    return render_template('index.html')


@usuario.route('/registros', methods=['GET'])
def registros():
    return render_template('registros.html')


@usuario.route('/usuarios', methods=['GET'])
def usuarios():
    usuarios = User.query.all()
    lista = []
    for i in usuarios:
        dic = {}
        dic["nombre"] = i.nombre
        dic["correo"] = i.correo
        dic["ciudad"] = i.ciudad
        lista.append(dic)
   # print(usuarios[0].nombre)
    return jsonify({"datos": lista[]})
