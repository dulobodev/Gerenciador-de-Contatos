from models.models import Contato
from flask import jsonify
from flask import json
from flask import request
from data_base import db


def Create(contato_data):
    novo_contato = Contato(
        nome=contato_data['nome'],  
        email=contato_data['email'],    
        telefone=contato_data['telefone'],
        categoria=contato_data['categoria']
          
    )     
    db.session.add(novo_contato)
    db.session.commit()
    response = [{'mensagem' : 'Contato criado com sucesso.', 'dados' : novo_contato.json()}]
    return jsonify(response), 200


# Buscar todos os contatos
def Read():
    contatos = Contato.query.all()

    if not contatos:
        response =  [{'mensagem' : 'Erro'}]
        return jsonify(response)
    
    response = [{'mensagem': 'Lista de contatos.','dados': [contato.json() for contato in contatos]}]
    return jsonify(response), 200

def Read_by_id(contato_id):
    contato = Contato.query.get(contato_id)

    if not contato:
        response = [{'mensagem': 'contato nao encontrado'}]
        return jsonify(response), 404

    response = [{'mensagem' : 'Contato encontrado com sucesso', 'dados' : contato.json()}]  
    return jsonify(response), 200

def Read_by_name(nome_contato):
    contato = Contato.query.filter_by(nome=nome_contato).first()

    if not contato:
        response = {{'mensagem' : 'Contato nao encontrado'}}
        return jsonify(response), 404
    
    response = [{'mensagem' : 'Contato encontrado com sucesso', 'dados' : contato.json()}]
    return jsonify(response), 200
        
def Update(id, contato_data):  
    contato = Contato.query.get(id)  # Busca o contato pelo ID  

    if not contato:  # Se o contato não for encontrado, retorna erro  
        response = [{'mensagem': 'contato não encontrado.'}]
        return jsonify(response), 404

    # Valida se todos os campos obrigatórios foram fornecidos  
    if not all(key in contato_data for key in ['nome', 'email', 'telefone', 'categoria']):  
        response = [{'mensagem': 'Dados inválidos. [nome], [email], [telefone] e [categoria] são obrigatórios.'}] 
        return jsonify(response), 400

    

    # Atualiza os campos do contatos
    contato.nome=contato_data['nome']
    contato.email=contato_data['email']   
    contato.telefone=contato_data['telefone']
    contato.categoria=contato_data['categoria']
    
    db.session.commit()  

    response = [{'mensagem' : 'Atualizacao de contato feita com sucesso'}]
    return jsonify(response), 200

def Delete(contato_id):
    confirmacao = request.args.get('confirmacao')
    contato = Contato.query.get(contato_id)


    if confirmacao == 'true':
        db.session.delete(contato)
        db.session.commit()

        response = [{'mensagem' : 'anime deletado com sucesso'}]
        return jsonify(response), 200
    else:
        response = [{'mensagem' : 'anime não encontrado'}]
        return jsonify(response), 404