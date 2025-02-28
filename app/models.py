from app import db
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash


class Contato(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    dataenv = db.Column(db.DateTime, default=datetime.now())
    nome = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    telefone = db.Column(db.String, nullable=False)
    mensagem = db.Column(db.String, nullable=False)

class Login(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String, nullable=False)    
    senha = db.Column(db.String, nullable=False)    

    def set_password(self, password):
        """Criptografa a senha antes de armazenar no banco de dados."""
        self.senha = generate_password_hash(password)

    def check_password(self, password):
        """Verifica se a senha digitada corresponde ao hash armazenado."""
        return check_password_hash(self.senha, password)
    
class Cursos(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String, nullable=False) 
    lugar = db.Column(db.String, nullable=False) 

class Habilidades(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String, nullable=False) 
    nivel = db.Column(db.String, nullable=False) 
