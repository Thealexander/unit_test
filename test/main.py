import psycopg2
import os 
import json
import pprint
connection = psycopg2.connect(
    host = "192.168.1.9",
    user = "usuario",
    password = "home.1705",
    database = "pruebas_tecnicas",
    port = "5432"
)
connection.autocommit = True

def crear_tabla_persona():
    cursor = connection.cursor()
    query = """create table if not exist persona (id serial primary key, nombre varchar(60), identificacion varchar(60), ciudad_id integer, email varchar(60),
                sexo varchar(60), universidad_id integer,
                CONSTRAINT fx_universidad FOREIGN KEY(universidad_id) references universidad(id),
                CONSTRAINT fx_ciudad FOREIGN KEY(ciudad_id) references ciudad(id));"""
    cursor.execute(query)
    pass
def crear_tabla_universidad():
    cursor = connection.cursor()
    query = """create table if not exist universidad(id serial primary key, nombre varchar(100));"""
    cursor.execute(query)
    pass
def crear_tabla_ciudad():
    cursor = connection.cursor()
    query = """create table if not exist ciudad (id serial primary key, nombre varchar(100));"""
    cursor.execute(query)
    pass
def crear_tablas():
    crear_tabla_ciudad()
    crear_tabla_universidad()
    crear_tabla_persona()
def insertar_universidad():
    ##para reemplazar comillas
    universidad = universidad.replace("'",'')
    #print(universidad)
    cursor = connection.cursor()
    query = f"""SELECT * FROM universidad where nombre = '{universidad}' ;"""
    cursor.execute(query)
    row = cursor.fetchone()
    if cursor.fetchone() is none:
        query = f"""INSERT INTO unversidad(nombre) values('{universidad}') ;"""
        cursor.execute(query)
    query = f"""SELECT * FROM universidad where nombre = '{universidad}'; """
    cursor.execute(query)
    id_universidad = cursor.fetchone()[0]
    #print(id_universidad[0])
    cursor.close()
    return id_universidad
    #pass
def insertar_ciudad(ciudad):
     ##para reemplazar comillas
    universidad = universidad.replace("'",'')
    #print(universidad)
    cursor = connection.cursor()
    query = f"""SELECT * FROM ciudad where nombre = '{ciudad}' ;"""
    cursor.execute(query)
    row = cursor.fetchone()
    if cursor.fetchone() is none:
        query = f"""INSERT INTO ciudad(nombre) values('{ciudad}') ;"""
        cursor.execute(query)
    query = f"""SELECT * FROM ciudad where nombre = '{ciudad}'; """
    cursor.execute(query)
    id_ciudad = cursor.fetchone()[0]
    #print(id_universidad[0])
    cursor.close()
    return id_ciudad
    #pass
def persona(nombre,identificacion,ciudad_id,email,sexo,universidad_id):
    cursor = connection.cursor()
    query = f""" INSERT INTO persona(nombre, identificacion, ciudad_id, email, sexo, universidad_id)
    values
    ('{nombre}','{identificacion}','{ciudad_id}','{email}','{sexo}','{universidad_id}')
    """
    cursor.execute(query)
    cursor.close()
def leer_json():
    directorio = os.getcwd()()
    lista = []
    with os.scandir(path=directorio) as itr:
        archivos_json = [i for i in itr if i.is_file() and "informacion" in i.name.split(".")[0] and ar.name.split('.')[1]=="json"]
      #  print(archivos_json)
        for i in archivos_json:
            f = open(i,encoding="utf-8")
            data = json.load(f)
            pprint(data)
            ###
            print(type(data))
            for j in data:
                print(j[nombre],j[identificacion])
                id_universidad = insertar_universidad(j["universidad"])
                id_ciudad = insertar_ciudad(j["ciudad"])
                persona = (j["nombre"],j["identificacion"],id_ciudad,j["email"],j["sexo"],id_universidad)
                #break
            ###
            f.close()
          #  break

    #    for ar in itr:
     #       print(ar,ar.is_file(),ar.name)
      #      if ar.is_file() and "informacion" in ar.name.split(".")[0] and ar.name.split('.')[1]=="json":
       #         lista.append(ar.name)
        #        print(lista)
    #print(directorio)
   # pass
if __name__ =="__main__":
    crear_tablas()