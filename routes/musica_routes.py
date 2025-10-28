from flask import Blueprint, request 
from controllers.musica_controllers import (
    get_musicas,
    get_musica_by_id,
    get_musica_by_nome,
    create_musica,
    update_musica,
    delete_musica
)

# Define um Blueprint para as rotas de "Música"
musica_routes = Blueprint('musica_routes', __name__)  

# Rota para listar todas as músicas (GET)
@musica_routes.route('/musicas', methods=['GET'])
def musicas_get():
    return get_musicas()

# Rota para buscar uma música pelo ID (GET)
@musica_routes.route('/musicas/<int:musica_id>', methods=['GET'])
def musica_get_by_id(musica_id):
    return get_musica_by_id(musica_id)

# Rota para buscar uma música pelo nome (GET)
@musica_routes.route('/musicas/nome/<string:musica_nome>', methods=['GET'])
def musica_get_by_nome(musica_nome):
    return get_musica_by_nome(musica_nome)

# Rota para criar uma nova música (POST)
@musica_routes.route('/musicas', methods=['POST'])
def musicas_post():
    return create_musica(request.json)

# Rota para atualizar uma música pelo ID (PUT)
@musica_routes.route('/musicas/<int:musica_id>', methods=['PUT'])
def musicas_put(musica_id):
    return update_musica(musica_id, request.json)

# Rota para excluir uma música pelo ID (DELETE)
@musica_routes.route('/musicas/<int:musica_id>', methods=['DELETE'])
def musica_delete(musica_id):
    return delete_musica(musica_id)
