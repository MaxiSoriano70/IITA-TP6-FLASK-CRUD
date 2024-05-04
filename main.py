from flask import Flask, jsonify, request
import dbCarnetVet

app = Flask(__name__)

@app.route("/")
def index():
    return "Index de CarnetVet"

"""TODOS LOS USUARIOS"""
@app.route("/CarnetVet/api/usuarios", methods=["GET"])
def get_usuarios():
    usuarios = dbCarnetVet.get_usuarios_bd()
    if(usuarios):
        return jsonify(usuarios), 200
    else:
        return jsonify(message="Usuarios not found"), 404

"""AGREGAR USUARIO"""
@app.route("/CarnetVet/api/usuarios", methods=["POST"])
def create_usuario():
    usuario = request.json
    if(dbCarnetVet.post_usuario_bd(usuario)):
        return jsonify(message="Usuario created successfully"), 200
    else:
        return jsonify(message="Usuarios created not found"), 404

"""OBTENER UN USUARIO"""
@app.route("/CarnetVet/api/usuarios/<int:usuario_id>", methods=["GET"])
def get_usuario_id(usuario_id):
    usuarioEncontrado = dbCarnetVet.get_usuario_id_db(usuario_id)
    if(usuarioEncontrado):
        return jsonify(usuarioEncontrado), 200
    else:
        return jsonify(message="Usuario not found"), 404

"""ACTUALIZAR UN USUARIO"""
@app.route("/CarnetVet/api/usuarios/<int:usuario_id>", methods=["PUT"])
def update_usuario_id(usuario_id):
    datosNuevosUsuario = request.json
    usuarioCambios = dbCarnetVet.update_usuario_id_db(datosNuevosUsuario, usuario_id)
    if(usuarioCambios):
        return jsonify(message="Usuario update successfully"), 200
    else:
        return jsonify(message="Usuario not found"), 404

"""ELIMINAR USUARIO"""
@app.route("/CarnetVet/api/usuarios/<int:usuario_id>", methods=["DELETE"])
def delete_usuario_id(usuario_id):
    usuarioEliminado = dbCarnetVet.delete_usuario_id_db(usuario_id)
    if(usuarioEliminado):
        return jsonify(message="Usuario delete successfully"), 200
    else:
        return jsonify(message="Usuario not found"), 404

if __name__ == "__main__":
    app.run()