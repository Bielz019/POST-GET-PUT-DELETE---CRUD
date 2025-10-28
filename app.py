from flask import Flask
from db import db  # Importa a instância do banco
from routes.musica_routes import musica_routes  # Importa as rotas de músicas

def create_app():
    app = Flask(__name__)

    # Configuração do banco de dados (exemplo com SQLite)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///musicas.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Inicializa o banco de dados
    db.init_app(app)

    # Registra as rotas de música
    app.register_blueprint(musica_routes)

    @app.route('/')
    def index():
        return {'mensagem': 'API de músicas funcionando 🎵'}

    return app

if __name__ == '__main__':
    app = create_app()
    
    # Cria as tabelas no banco (caso ainda não existam)
    with app.app_context():
        db.create_all()
    
    # Inicia o servidor Flask
    app.run(debug=True)
