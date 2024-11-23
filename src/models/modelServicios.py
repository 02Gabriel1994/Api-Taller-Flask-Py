
class ModelServicios():
    @classmethod
    def Buscar_Servicio(self,db,datos):
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
    def Registrar_Servicio(self,db,datos):
        try:
            cursor=db.connection.cursor()
            sql = """INSERT INTO Servicios (fecha_ingreso, fecha_salida, placa, estado_entrada, trabajo_a_realizar)
                    VALUES (%s, %s, %s,%s, %s);"""
            cursor.execute(sql,(datos.fecha_ingreso, datos.fecha_salida ,datos.placa, datos.estado_entrada , datos.trabajo_a_realizar))
            db.connection.commit()
            return True
        except Exception as ex:
            error_message = str(ex)
            # if "Duplicate entry" in error_message:  # Verificamos si el error es un "Duplicate entry"
            #     return 1062
            # else:
            return error_message  # Para cualquier otro error
   