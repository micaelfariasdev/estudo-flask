from app import db
from app.models import Login
from werkzeug.security import generate_password_hash

def create_admin():
    admin_name = "admin"
    admin_password = "@ADmin9977"

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
