from flask_wtf import FlaskForm
from wtforms import *
from wtforms.validators import *
from app import db
from app.models import *


class ContatoForms(FlaskForm):
    nome = StringField("Nome", validators=[DataRequired()], render_kw={"placeholder":"Nome"})
    email = StringField("E-mail", validators=[DataRequired(), Email()], render_kw={"placeholder":"E-mail"})
    telefone = TelField("Telefone", validators=[DataRequired()], render_kw={"placeholder":"Telefone"})
    msg = TextAreaField("Mensagem", validators=[DataRequired()], render_kw={"placeholder":"Mensagem"})
    buttomSubmit = SubmitField("Enviar", render_kw={"id":"botão-contato"})
    
    def save(self):
        contato = Contato(
            nome = self.nome.data,
            email = self.email.data,
            telefone = self.telefone.data,
            mensagem = self.msg.data
        )

        db.session.add(contato)
        db.session.commit()

class LoginForm(FlaskForm):
    usuario = StringField('Usuario', validators=[DataRequired()])
    senha = PasswordField('Senha', validators=[DataRequired()])
    buttomSubmit = SubmitField("Entrar")

class CursoForm(FlaskForm):
    nome = StringField('nome', validators=[DataRequired()])
    lugar = StringField('lugar', validators=[DataRequired()])
    buttomSubmit = SubmitField("Adicionar")

    def save(self):
        curso = Cursos(
            nome = self.nome.data,
            lugar = self.lugar.data,
            
        )

        db.session.add(curso)
        db.session.commit()

class HabilidadeForm(FlaskForm):
    nome = StringField('nome', validators=[DataRequired()])
    nivel = StringField('nivel', validators=[DataRequired()])
    buttomSubmit = SubmitField("Adicionar")

    def save(self):
        hab = Habilidades(
            nome = self.nome.data,
            nivel = self.nivel.data,
           
        )

        db.session.add(hab)
        db.session.commit()


