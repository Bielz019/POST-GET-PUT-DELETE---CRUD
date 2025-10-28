# Importa o objeto `db` que representa a conexão com o banco de dados
from db import db

# Define a classe Musica como um modelo de dados do SQLAlchemy
class Musica(db.Model):
    # Define o nome da tabela no banco de dados
    __tablename__ = 'musicas'

    # Define a estrutura da tabela com suas colunas
    id = db.Column(db.Integer, primary_key=True)  # Coluna ID, chave primária
    nome = db.Column(db.String(100), nullable=False)  # Nome da música
    artista = db.Column(db.String(100), nullable=False)  # Nome do artista
    genero = db.Column(db.String(50), nullable=False)  # Gênero musical

    # Método para converter o objeto em formato JSON
    def json(self):
        return {
            'id': self.id,
            'nome': self.nome,
            'artista': self.artista,
            'genero': self.genero
        }
