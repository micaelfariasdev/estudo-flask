from app import app, db
from flask import render_template, url_for, request, redirect, flash, session
from app.models import Contato, Login, Cursos, Habilidades
from app.forms import *
from werkzeug.security import generate_password_hash, check_password_hash


@app.route('/')
def index():
    cursos = Cursos.query.order_by(Cursos.nome).all()
    habidade = Habilidades.query.order_by(Habilidades.nome).all()
    return render_template('index.html', cursos=cursos, habidade=habidade)

@app.route('/contato/', methods=['GET', 'POST'])
def contato():
    form = ContatoForms()
    if form.validate_on_submit():
        form.save()
        return redirect(url_for('contato')) 

    return render_template('contato.html', form=form)

@app.route('/admin/', methods=['GET', 'POST'])
def admin():
    form = LoginForm()
    
    if form.validate_on_submit():
        usuario = form.usuario.data
        senha = form.senha.data

        # Buscar usuário no banco de dados
        user = Login.query.filter_by(nome=usuario).first()

        if user and user.check_password(senha):  # Verifica se a senha está correta
            session['nome'] = usuario
            flash("Login bem-sucedido!", "success")
            return redirect(url_for('index'))  # Redireciona para o painel
        else:
            flash("Usuário ou senha incorretos!", "danger")

    return render_template('admin.html', form=form)

@app.route('/dashboard/', methods=['GET', 'POST'])
def DashBoard():
    cursos = Cursos.query.order_by(Cursos.nome).all()
    habidade = Habilidades.query.order_by(Habilidades.nome).all()   # Consulta dos cursos
    

    if 'nome' not in session or session['nome'] != 'admin':
        flash('Acesso restrito. Você precisa estar logado como administrador.', 'danger')
        return redirect(url_for('login'))  # Redireciona para a página de login

    cursoform = CursoForm()
    if cursoform.validate_on_submit():
        cursoform.save()
        return redirect(url_for('DashBoard'))

         

    habform = HabilidadeForm()
    if habform.validate_on_submit():
        habform.save()
        return redirect(url_for('DashBoard'))
    return render_template('deshboard.html', habidade=habidade, dados=cursos, habform=habform, cursoform=cursoform)  # Passa 'dados' como contexto

@app.route('/deletecurso/<int:id>', methods=['POST'])
def delete_curso(id):
    curso = Cursos.query.get_or_404(id)  # Busca o curso pelo ID ou retorna 404
    db.session.delete(curso)  # Remove do banco de dados
    db.session.commit()  # Salva a alteração
    flash('Curso deletado com sucesso!', 'success')
    return redirect(url_for('DashBoard'))  # Redireciona para o dashboard

@app.route('/deletehabilidade/<int:id>', methods=['POST'])
def delete_habilidade(id):
    curso = Habilidades.query.get_or_404(id)  # Busca o curso pelo ID ou retorna 404
    db.session.delete(curso)  # Remove do banco de dados
    db.session.commit()  # Salva a alteração
    flash('Curso deletado com sucesso!', 'success')
    return redirect(url_for('DashBoard')) 

@app.route('/#logout')
def logout():
    session.clear()  # Remove todos os dados da sessão
    flash("Você foi desconectado.", "success")
    return redirect(url_for('index'))

@app.errorhandler(404)
def error(e):
    erro = 'e404'
    return render_template('erro404.html', erro = erro ), 404