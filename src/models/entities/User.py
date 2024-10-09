from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import UserMixin #Esto es para revisar si el usuario esta activo o no entre otras funciones
class User(UserMixin):
    def __init__(self, id, username, password, fullname = "") -> None:
        self.id = id
        self.username = username
        self.password = password
        self.fullname= fullname
    @classmethod # esto es que se hace sin instanciar la clase.
    def check_password(self, hashed_password, pasword):
        return check_password_hash(hashed_password,pasword)
    

