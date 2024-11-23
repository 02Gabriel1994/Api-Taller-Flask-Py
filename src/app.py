#https://youtu.be/FX0lMm_Qj10
from flask import Flask, render_template, request, redirect, url_for, flash
from config import config
from flask_mysqldb import MySQL
from flask_login import LoginManager, login_user, logout_user, login_required # esto es para manejo de seciones
from models.ModelUser import ModelUser
from models.entities.User import User
from models.entities.Clientes import clientes
from models.modelClientes import ModelCliente
from models.entities.vehiculo import EntitiVehiculo
from models.modelVehiculo import ModelVehiculo
from models.entities.Servicios import EntitiServicios
from models.modelServicios import ModelServicios
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
@app.route('/cliente', methods=['GET', 'POST'])
def cliente():
    if request.method == 'POST':
        options = {
        "1": "Tarjeta de Identidad",
        "2": "Cedula de ciudadania",
        "3": "Cedula de extranjeria",
        "4": "Pasaporte"
    }
        Nombre = request.form['nombre']
        tipoDeIdentificacion = options.get(request.form['tipo_identificacion'], 0) 
        Apellidos = request.form['Apellidos']
        fecha= request.form['Fecha']
        Documento= request.form['Documento']
        email = request.form['email']
        telefono =request.form['Telefono']
        direcicion = request.form['Direccion']
        ciudad = request.form['Ciudad']
        Datos =clientes(Nombre, tipoDeIdentificacion, Apellidos, fecha, Documento, email, telefono, direcicion, ciudad)
        registrarCliente=ModelCliente.Registrar(db,Datos )
        if registrarCliente ==  1062:
            flash("Cliente Ya existe")
        elif registrarCliente == True:
            flash("Grabado con Exito")
        else:
            flash(f"Error al guardar{registrarCliente}")
    return render_template('cliente.html')
@app.route('/vehiculo', methods=['GET', 'POST'])
def vehiculo():
    if request.method == 'POST':
        options = {
        "1": "Sedán",
        "2": "Hatchback",
        "3": "SUV",
        "4": "Pickup",\
        "5": "Convertible",
        "6": "Coupé",
        "7": "Minivan",
        "8": "Van",
        "9": "Motocicleta",
        "10": "Camion",
        "11": "Autobús",
        "12": "Tractor",
        "13": "Trailler",
    }
        cedula = request.form['cedula']
        tipo_vehiculo = options.get(request.form['tipo_vehiculo'], 0) 
        marca = request.form['marca']
        modelo= request.form['modelo']
        año= request.form['año']
        placa = request.form['placa']
        color =request.form['color']
        mensaje = request.form['mensaje']
        Datos = EntitiVehiculo(cedula, marca, tipo_vehiculo, modelo,año, placa, color, mensaje)
        #dato=ModelCliente.Registrar(db,Datos )
        if ModelCliente.buscarCliente(db, Datos.cedula) ==  True:
            respuesta = ModelVehiculo.Registrar_Vehiculo(db,Datos)
            if respuesta == True:
                flash("Grabado con Exito")
            else:
                flash(f"Error al guardar{respuesta}")
        else:
            flash(f"Cliente no existe, debe registrarlo primero.")
    return render_template('Vehiculo.html')
@app.route('/servicios', methods=['GET', 'POST'])
def servicios():
    if request.method == 'POST':
        Fecha_Ingreso = request.form['Fecha_Ingreso']
        Fecha_Salida = request.form['Fecha_Salida']
        if Fecha_Salida == "" :
            Fecha_Salida = "20010101"

        placa= request.form['placa']
        Estado_Entrada= request.form['Estado_Entrada']
        Trabajo_Realizado = request.form['Trabajo_Realizado']
        Datos = EntitiServicios(Fecha_Ingreso, Fecha_Salida, placa, Estado_Entrada,Trabajo_Realizado)
        #dato=ModelCliente.Registrar(db,Datos )
        if ModelVehiculo.Buscar_Vehiculo(db, Datos.placa) ==  True:
            respuesta = ModelServicios.Registrar_Servicio(db,Datos)
            if respuesta == True:
                flash("Grabado con Exito")
            else:
                flash(f"Error al guardar{respuesta}")
        else:
            flash(f"vehiculo no existe, debe registrarlo primero.")
    return render_template('servicios.html')
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