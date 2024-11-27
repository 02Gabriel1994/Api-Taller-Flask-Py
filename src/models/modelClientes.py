

class ModelCliente():
    @classmethod
    def buscarCliente(self,db,cedula):
        try:
            cursor=db.connection.cursor()
            sql = """Select * from clientes where documento = %s;"""
            cursor.execute(sql,(cedula,))
            row =cursor.fetchone()
            if not row == None:
                return row
            else:
                return None
        except Exception as ex:
            raise Exception(ex)
    @classmethod
    def Registrar(self,db,datos):
        try:
            cursor=db.connection.cursor()
            sql = """INSERT INTO Clientes (nombre, tipoDeIdentificacion, apellidos, fecha, documento, email, telefono, direccion, ciudad)
                    VALUES (%s, %s, %s,%s, %s, %s, %s, %s, %s);"""
            cursor.execute(sql,(datos.Nombre, datos.tipoDeIdentificacion ,datos.Apellidos , datos.fecha, datos.Documento, datos.email, datos.telefono ,datos.direcicion ,datos.ciudad ))
            db.connection.commit()
            return True
        except Exception as ex:
            error_message = str(ex)
            if "Duplicate entry" in error_message:  # Verificamos si el error es un "Duplicate entry"
                return 1062
            else:
                return error_message  # Para cualquier otro error
    @classmethod
    def Modificar(self,db,datos):
        try:
            cursor=db.connection.cursor()
            sql = """UPDATE Clientes
                    SET 
                        nombre = %s,
                        tipoDeIdentificacion = %s,
                        apellidos = %s,
                        fecha = %s,
                        email = %s,
                        telefono = %s,
                        direccion = %s,
                        ciudad = %s
                    WHERE 
                        documento = %s; 
                    ;"""
            cursor.execute(sql,(datos.Nombre, datos.tipoDeIdentificacion ,datos.Apellidos , datos.fecha, datos.email, datos.telefono ,datos.direcicion ,datos.ciudad, datos.Documento ))
            db.connection.commit()
            return True
        except Exception as ex:
            error_message = str(ex)
            if "Duplicate entry" in error_message:  # Verificamos si el error es un "Duplicate entry"
                return 1062
            else:
                return error_message  # Para cualquier otro error
     