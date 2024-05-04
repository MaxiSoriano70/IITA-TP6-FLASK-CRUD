import psycopg2
import json

conn = psycopg2.connect(
    user="postgres", password="1234", port="5432", host="localhost", database="DB_CarnetVet"
)

cursor = conn.cursor()

def get_usuarios_bd():
    cursor.execute("SELECT * FROM usuarios")
    column_names = [desc[0] for desc in cursor.description]

    usuarios = []
    for row in cursor.fetchall():
        usuario = dict(zip(column_names, row))
        usuarios.append(usuario)
    return usuarios

def post_usuario_bd(usuario):
    consultaSql = "INSERT INTO usuarios (nombreApellido, email, telefono, fechaNacimiento, contrasenia) VALUES (%s, %s, %s, %s, %s)"
    valores = list(usuario.values())
    try:
        cursor.execute(consultaSql, valores)
        conn.commit()
        return True
    except Exception as e:
        print("Error al insertar usuario:", e)
        conn.rollback()
        return False

def get_usuario_id_db(id):
    consultaSql = "SELECT * FROM usuarios WHERE idUsuario = %s"
    valores = (id,)
    cursor.execute(consultaSql, valores)
    column_names = [desc[0] for desc in cursor.description]
    usuario = {}
    resultado = cursor.fetchone()
    if resultado:
        usuario = dict(zip(column_names, resultado))
    return usuario

def update_usuario_id_db(datos, id):
    datos['idUsuario'] = id
    consultaSql = "UPDATE usuarios SET nombreApellido = %(nombreApellido)s, email = %(email)s, telefono = %(telefono)s, fechaNacimiento = %(fechaNacimiento)s, contrasenia = %(contrasenia)s WHERE idUsuario = %(idUsuario)s"
    try:
        cursor.execute(consultaSql, datos)
        conn.commit()
        return True
    except Exception as e:
        print("Error al actualizar usuario:", e)
        conn.rollback()
        return False

def delete_usuario_id_db(id):
    consultaSql = "DELETE FROM usuarios WHERE idUsuario = %s"
    try:
        cursor.execute(consultaSql, (id,))
        conn.commit()
        return True
    except Exception as e:
        print("Error al eliminar usuario:", e)
        conn.rollback()
        return False

