from models.musica_models import Musica  # Importa o modelo Musica
from db import db  # Importa a conexão com o banco de dados
import json
from flask import make_response, request

# Função para obter todas as músicas
def get_musicas():
    musicas = Musica.query.all()  # Busca todas as músicas no banco de dados
    
    if not musicas:  # Verifica se a lista de músicas está vazia
        response = make_response(
            json.dumps({
                'mensagem': 'Nenhuma música encontrada.',
                'dados': []  # Nenhuma música encontrada
            }, ensure_ascii=False, sort_keys=False)
        )
    else:
        response = make_response(
            json.dumps({
                'mensagem': 'Lista de músicas.',
                'dados': [musica.json() for musica in musicas]  # Converte os objetos de música para JSON
            }, ensure_ascii=False, sort_keys=False)
        )
    
    response.headers['Content-Type'] = 'application/json'
    return response


# Função para obter uma música específica por ID
def get_musica_by_id(musica_id):
    musica = Musica.query.get(musica_id)  # Busca a música pelo ID

    if musica:
        response = make_response(
            json.dumps({
                'mensagem': 'Música encontrada.',
                'dados': musica.json()
            }, ensure_ascii=False, sort_keys=False)
        )
        response.headers['Content-Type'] = 'application/json'
        return response
    else:
        response = make_response(
            json.dumps({'mensagem': 'Música não encontrada.', 'dados': {}}, ensure_ascii=False),
            404
        )
        response.headers['Content-Type'] = 'application/json'
        return response


# Função para consultar uma música por nome
def get_musica_by_nome(musica_nome):
    musica = Musica.query.filter_by(nome=musica_nome).first()  # Busca a música pelo nome

    if musica:
        response = make_response(
            json.dumps({
                'mensagem': 'Música encontrada.',
                'dados': musica.json()
            }, sort_keys=False)
        )
        response.headers['Content-Type'] = 'application/json'
        return response
    else:
        response = make_response(
            json.dumps({
                'mensagem': 'Música não encontrada.',
                'dados': {}
            }, sort_keys=False)
        )
        response.headers['Content-Type'] = 'application/json'
        return response, 404


# Função para criar uma nova música
def create_musica(musica_data):
    # Valida se todos os campos obrigatórios foram fornecidos
    if not all(key in musica_data for key in ['nome', 'artista', 'genero']):
        response = make_response(
            json.dumps({'mensagem': 'Dados inválidos. Nome, artista e gênero são obrigatórios.'}, ensure_ascii=False),
            400
        )
        response.headers['Content-Type'] = 'application/json'
        return response
    
    # Cria a nova música
    nova_musica = Musica(
        nome=musica_data['nome'],
        artista=musica_data['artista'],
        genero=musica_data['genero']
    )
    
    db.session.add(nova_musica)
    db.session.commit()

    # Resposta de sucesso com os dados da nova música
    response = make_response(
        json.dumps({
            'mensagem': 'Música cadastrada com sucesso.',
            'musica': nova_musica.json()
        }, ensure_ascii=False, sort_keys=False)
    )
    response.headers['Content-Type'] = 'application/json'
    return response


# Função para atualizar uma música por ID
def update_musica(musica_id, musica_data):
    musica = Musica.query.get(musica_id)

    if not musica:
        response = make_response(
            json.dumps({'mensagem': 'Música não encontrada.'}, ensure_ascii=False),
            404
        )
        response.headers['Content-Type'] = 'application/json'
        return response

    # Valida campos obrigatórios
    if not all(key in musica_data for key in ['nome', 'artista', 'genero']):
        response = make_response(
            json.dumps({'mensagem': 'Dados inválidos. Nome, artista e gênero são obrigatórios.'}, ensure_ascii=False),
            400
        )
        response.headers['Content-Type'] = 'application/json'
        return response

    # Atualiza os dados da música
    musica.nome = musica_data['nome']
    musica.artista = musica_data['artista']
    musica.genero = musica_data['genero']

    db.session.commit()

    response = make_response(
        json.dumps({
            'mensagem': 'Música atualizada com sucesso.',
            'musica': musica.json()
        }, ensure_ascii=False, sort_keys=False)
    )
    response.headers['Content-Type'] = 'application/json'
    return response


# Função para excluir uma música por ID com confirmação via parâmetro
def delete_musica(musica_id):
    confirmacao = request.args.get('confirmacao')

    if confirmacao != 'true':
        response = make_response(
            json.dumps({'mensagem': 'Confirmação necessária para excluir a música.'}, ensure_ascii=False),
            400
        )
        response.headers['Content-Type'] = 'application/json'
        return response

    musica = Musica.query.get(musica_id)
    if not musica:
        response = make_response(
            json.dumps({'mensagem': 'Música não encontrada.'}, ensure_ascii=False),
            404
        )
        response.headers['Content-Type'] = 'application/json'
        return response

    db.session.delete(musica)
    db.session.commit()

    response = make_response(
        json.dumps({'mensagem': 'Música excluída com sucesso.'}, ensure_ascii=False, sort_keys=False)
    )
    response.headers['Content-Type'] = 'application/json'
    return response
