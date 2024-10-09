#https://youtu.be/FX0lMm_Qj10
from flask import Flask, render_template, request, redirect, url_for, flash
from config import config
from flask_mysqldb import MySQL
from flask_login import LoginManager, login_user, logout_user, login_required # esto es para manejo de seciones
from models.ModelUser import ModelUser
from models.entities.User import User
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__) # crea la instancia de flask
crsf = CSRFProtect()
db = MySQL(app) # esto va a ser el cursor para hacer el crud
login_manager_app = LoginManager(app) # Manejo de seciones
@login_manager_app.user_loader
def load_user(id): # Esta funcion es para poder cargar las caracteristicas del usuario logueado, sino genera error
    return ModelUser.get_by_id(db, id)
@app.route('/')
def index():
    return redirect(url_for('login'))
@app.route('/login', methods=['GET', 'POST'] )
def login():
    if request.method == 'POST': #Hay dos metodos el get que es cuando recien se entra, y el post, que es cuando se pide el login, aqui se hara la parte de cuando se esta pidiendo ese login
        print(request.form['usuario'])
        print(request.form['password'])
        user =User(0,request.form['usuario'], request.form['password'] )
        logged_user=ModelUser.login(db, user)
        if not logged_user == None:
            if logged_user.password:
                login_user(logged_user) # Este es para mantenerlo como usuario logueado, control de seciones
                return redirect(url_for('home'))
            else:
                flash("Contraseña invalida")
                return render_template('auth/login.html')
        else:
            if not request.form['usuario'] == "":
                flash("El usuario No existe")
            return render_template('auth/login.html')
    else:
        
        return render_template('auth/login.html')
@app.route('/logout') # Cerrar la app bien
def logout():
    logout_user()
    return redirect(url_for('login'))
@app.route('/home')
def home():
    return render_template('home.html')
@app.route('/protegido') #asi se protege de accesos sin logueo
@login_required # esto indica que requiere que este logueado para acceder
def protected():
    return "<h1>Esto es una vista protegida, solo para logueados</h1>"
def status_401(error):#Esto hara que si no esta autorizado lo redirecione aqui
    return redirect(url_for('login'))
def status_404(error): #Por si escribe algo que no existe, y estos errores deben estar mapeados en el main
    return "<h1>Sitio no encontrado</h1>"
if __name__ == '__main__': # este es como el main de java
    
    app.config.from_object(config['development'])
    crsf.init_app(app)
    app.register_error_handler(401,status_401) #Le estoy didciendo que si sale error 401 se vaya a la funcion status_401, lo mismo abajo
    app.register_error_handler(404,status_404)
    app.run()