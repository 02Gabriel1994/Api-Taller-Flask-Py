from models.entities.User import User

class ModelUser():
    @classmethod
    def login(self,db,user):
        try:
            cursor=db.connection.cursor()
            sql = """SELECT id, User, Password, fullname FROM usuarios WHERE user = '{}'""".format(user.username) #El format comprueba si el usuarioi esta
            cursor.execute(sql)
            row =cursor.fetchone()
            if not row == None:
                user = User(row[0], row[1], User.check_password(row[2], user.password), row[3])
                return user
            else:
                return None
        except Exception as ex:
            raise Exception(ex)
    @classmethod
    def get_by_id(self,db,id):
        try:
            cursor=db.connection.cursor()
            sql = """SELECT id, User, fullname FROM usuarios WHERE id = '{}'""".format(id) #El format comprueba si el usuarioi esta
            cursor.execute(sql)
            row =cursor.fetchone()
            if not row == None:
                user = User(row[0], row[1], None, row[2])
                return user
            else:
                return None
        except Exception as ex:
            raise Exception(ex)