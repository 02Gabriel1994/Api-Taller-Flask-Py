from datetime import date

def dias_de_garantia(fecha):
    hoy = date.today()
    fecha_salida = fecha
    diferencia = hoy - fecha_salida
    dias = diferencia.days
    garantia = 30 - dias
    if not garantia < 0:
        return (garantia)
    else:
        return (0)

def validar_datos(datos):
    if any(not getattr(datos, attr) for attr in vars(datos)): # Revisa si los atributos de la clase estan vacios
        return False