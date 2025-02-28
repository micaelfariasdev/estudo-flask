from app import create_app, db
from app.models import Login
from werkzeug.security import generate_password_hash
import os
load_dotenv()

def create_admin():
    # Cria o contexto do aplicativo
    app = create_app()

    # Contexto do aplicativo
    with app.app_context():
        admin_name = os.getenv("LOGIN")
        admin_password = os.getenv("SENHA")

        # Verifica se o admin já existe
        admin = Login.query.filter_by(nome=admin_name).first()
        if not admin:
            new_admin = Login(nome=admin_name, senha=generate_password_hash(admin_password))
            db.session.add(new_admin)
            db.session.commit()
            print("Conta de administrador criada com sucesso!")
        else:
            print("Conta de administrador já existe.")

if __name__ == "__main__":
    create_admin()
