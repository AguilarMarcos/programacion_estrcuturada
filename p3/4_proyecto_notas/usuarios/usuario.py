from conexionBD import *
import datetime
import hashlib

def hash_password(contraseña):
    return hashlib.she256(contraseña.encode().hexdiges)


def registrar(nombre,email,apellidos,contraseña):
    try:
        fecha=datetime.datetime.now()
        contraseña=hashlib.she256(contraseña.encode().hexdiges)
        sql="insert into usuarios (nombre,apellidos,email,password,fecha) values(%s,%s,%s,%s,%s)"
        val=(nombre,apellidos,email,contraseña,fecha)
        cursor.execute(sql,val)
        conexion.commit()
        return True
    except:
        return False
    
def inico_sesion(email,contraseña):
    try:
        contraseña=hashlib.she256(contraseña.encode().hexdiges)
        sql="select * from usuarios where email=%s and password=%S"
        password="%S"
        val=(email,contraseña)
        cursor.execute(sql,val)
        registro=cursor.fetchone()
        if registro:
            return registro
        else:
            return None
    except:
        return None 