from flask_login import UserMixin 
class clientes(UserMixin):
    def __init__(self, Nombre, tipoDeIdentificacion, Apellidos, fecha, Documento, email, telefono, direcicion, ciudad) -> None:
        self.Nombre = Nombre
        self.tipoDeIdentificacion = tipoDeIdentificacion
        self.Apellidos = Apellidos
        self.fecha= fecha
        self.Documento= Documento
        self.email= email
        self.telefono= telefono
        self.direcicion= direcicion
        self.ciudad= ciudad
    
  