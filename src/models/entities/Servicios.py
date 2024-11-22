from flask_login import UserMixin 
class EntitiServicios(UserMixin):
    def __init__(self, id, fecha_ingreso, fecha_salida, placa, estado_entrada, trabajo_a_realizar) -> None:
        self.id = id
        self.fecha_ingreso = fecha_ingreso
        self.fecha_salida= fecha_salida
        self.estado_entrada= estado_entrada
        self.trabajo_a_realizar= trabajo_a_realizar
        self.placa= placa
