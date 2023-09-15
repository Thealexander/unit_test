from utils.db import db

class User(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    nombre = db.Column(db.String(100))
    correo = db.Column(db.String(100))
    ciudad = db.Column(db.String(100))

    def __init__(self,nombre,correo,ciudad):
        self.nombre = nombre
        self.ciudad = ciudad
        self.correo = correo