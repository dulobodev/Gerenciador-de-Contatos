from flask import Blueprint, request  
from controllers.controllers import Create, Read, Update, Read_by_id, Read_by_name, Delete

contato_routes = Blueprint('contato_routes', __name__)  

@contato_routes.route('/contato', methods=['POST'])
def contato_post():
    return Create(request.json)

@contato_routes.route('/contato', methods=['GET'])
def contato_get():
    return Read()

@contato_routes.route('/contato/<int:id>', methods=['GET'])
def contato_get_by_id(id):
    return Read_by_id(id)

@contato_routes.route('/contato/<string:nome_contato>', methods=['GET'])
def conato_get_by_name(nome_contato):
    return Read_by_name(nome_contato)

@contato_routes.route('/contato/<int:id>', methods=['PUT'])
def contato_put(id):
    return Update(id, request.json)

@contato_routes.route('/Animes/<int:contato_id>', methods=['DELETE'])
def contato_delete(contato_id):
        return Delete(contato_id)