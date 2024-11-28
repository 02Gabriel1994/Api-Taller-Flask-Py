
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
    @classmethod
    def Buscar_Vehiculo_por_cedula(self,db,cedula):
        try:
            cursor=db.connection.cursor()
            sql = """Select t0.marca, t0.modelo_anio, t0.year, t0.placa, t0.color, t0.tipo_vehiculo, t2.estado_entrada, t2.trabajo_a_realizar,t2.fecha_ingreso, t2.fecha_salida from vehiculos T0
                INNER JOIN CLIENTES T1 ON T0.CEDULA_CLIENTE = T1.DOCUMENTO
                inner join servicios t2 On T0.placa = t2.placa
                where T1.DOCUMENTO =  %s;"""
            cursor.execute(sql,(cedula,))
            row =cursor.fetchall()
            if not row == None:
                return row
            else:
                return None
        except Exception as ex:
            error_message = str(ex)
            return error_message  # Para cualquier otro error