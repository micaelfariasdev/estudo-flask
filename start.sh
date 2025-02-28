#!/bin/sh
pip install -r requirements.txt

# Executar migrações do banco de dados
flask db upgrade

# Criar conta admin se não existir
python create_admin.py

# Iniciar o servidor
gunicorn -w 4 -b 0.0.0.0:$PORT wsgi:app
