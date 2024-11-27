
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
            sql = """INSERT INTO vehiculos (cedula_cliente, marca, tipo_vehiculo, Modelo_anio, placa, color, year)
                    VALUES (%s, %s, %s,%s, %s, %s, %s);"""
            cursor.execute(sql,(datos.cedula, datos.marca ,datos.Tipo, datos.Modelo , datos.placa, datos.color ,datos.year))
            db.connection.commit()
            return True
        except Exception as ex:
            error_message = str(ex)
            return error_message  # Para cualquier otro error
    @classmethod
    def Buscar_Vehiculo(self,db,dato):
        try:
            cursor=db.connection.cursor()
            sql = """Select * from vehiculos where placa = %s;"""
            cursor.execute(sql,(dato,))
            row =cursor.fetchone()
           
            if not row == None:
                return row
            else:
                return None
        except Exception as ex:
            error_message = str(ex)
            return error_message  # Para cualquier otro error
    @classmethod
    def Modificar_Vehiculo(self,db,datos):
        try:
            cursor=db.connection.cursor()
            sql = """UPDATE vehiculos 
                    SET 
                        edula_cliente = %s,
                        marca = %s, 
                        tipo_vehiculo = %s, 
                        Modelo_anio = %s, 
                        
                        color = %s, 
                        year = %s
                    WHERE 
                        placa = %s
                    ;"""
            cursor.execute(sql,(datos.cedula, datos.marca ,datos.Tipo, datos.Modelo , datos.color ,datos.year, datos.placa))
            db.connection.commit()
            return True
        except Exception as ex:
            error_message = str(ex)
            return error_message  # Para cualquier otro error