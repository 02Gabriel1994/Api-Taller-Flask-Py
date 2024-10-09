

class config:
    SECRET_KEY = 'Motorola2017+*1018/-46924-3' # va ayudar con algunos manejos de sesiones, envio de mensajes a tra vez de flash

class DevelopmentConfig(config):
    DEBUG = True # esto es para inciiar el servidor en modo debug, que entiendo que es para cuando se hace cambios , se reinicie solo
    MYSQL_HOST = 'localhost' 
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = 'motorola'
    MYSQL_DB = 'flaskcontacts'
config ={'development': DevelopmentConfig}