#!/bin/sh

# Executar migrações do banco de dados
flask db migrate
flask db upgrade

# Criar conta admin se não existir
python criarconta.py

# Iniciar o servidor
gunicorn -w 4 -b 0.0.0.0:$PORT wsgi:app
