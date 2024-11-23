
class ModelVehiculo():
    @classmethod
    def buscarCliente(self,db,datos):
        try:
            cursor=db.connection.cursor()
            sql = """Select * from clientes where documento = %s;"""
            cursor.execute(sql,(datos.documento))
            row =cursor.fetchone()
            if not row == None:
                return True
            else:
                return None
        except Exception as ex:
            raise Exception(ex)
    @classmethod
    def Registrar_Vehiculo(self,db,datos):
        try:
            cursor=db.connection.cursor()
            sql = """INSERT INTO vehiculos (cedula_cliente, marca, tipo_vehiculo, Modelo_anio, placa, color, estado, year)
                    VALUES (%s, %s, %s,%s, %s, %s, %s, %s);"""
            cursor.execute(sql,(datos.cedula, datos.marca ,datos.Tipo, datos.Modelo , datos.placa, datos.color,  datos.estado ,datos.year))
            db.connection.commit()
            return True
        except Exception as ex:
            error_message = str(ex)
            return error_message  # Para cualquier otro error
    @classmethod
    def Buscar_Vehiculo(self,db,datos):
        try:
            cursor=db.connection.cursor()
            sql = """Select * from vehiculos where placa = %s;"""
            cursor.execute(sql,(datos,))
            row =cursor.fetchone()
           
            if not row == None:
                return True
            else:
                return None
        except Exception as ex:
            error_message = str(ex)
            return error_message  # Para cualquier otro error