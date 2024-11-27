from flask_login import UserMixin 
class EntitiVehiculo(UserMixin):
    def __init__(self, cedula, marca, Tipo, Modelo, year, placa, color) -> None:
        self.cedula = cedula
        self.marca = marca
        self.Modelo= Modelo
        self.Tipo= Tipo
        self.year= year
        self.placa= placa
        self.color= color
  
    