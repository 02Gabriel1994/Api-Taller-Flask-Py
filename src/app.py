#https://youtu.be/FX0lMm_Qj10
from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
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
import utilidades.Funciones as F
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
@login_required
def cliente():
    if request.method == 'POST':
        options = {
        "1": "Tarjeta de Identidad",
        "2": "Cedula de ciudadania",
        "3": "Cedula de extranjeria",
        "4": "Pasaporte"
    }
        action = request.form.get('action') 
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
        if action == 'registrar':
            datos_completos= F.validar_datos(Datos)
            if not datos_completos == False:
                registrarCliente=ModelCliente.Registrar(db,Datos)
                if registrarCliente ==  1062:
                    flash("Cliente Ya existe")
                elif registrarCliente == True:
                    flash("Grabado con Exito")
                else:
                    flash(f"Error al guardar{registrarCliente}")
            else:
                flash(f"Faltaron Datos por llenar")
        elif action == 'modificar':
            datos_completos= F.validar_datos(Datos)
            if not datos_completos == False:
                respuesta = ModelCliente.buscarCliente(db,Datos.Documento)
                if not respuesta == None:
                    respuesta= ModelCliente.Modificar(db,Datos)
                    if respuesta == True:
                        flash(f"Modificado con Exito")
                    else:
                        flash(f"Error al guardar: {respuesta}")
                else:
                    flash(f"El cliente no existe")
            else:
                flash(f"Faltaron Datos por llenar")
        elif action == 'buscar':
                respuesta= ModelCliente.buscarCliente(db,Datos.Documento)
                return render_template('cliente.html', datos=respuesta )
    return render_template('cliente.html')
@app.route('/vehiculo', methods=['GET', 'POST'])
@login_required
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
        action = request.form.get('action') 
        cedula = request.form['cedula']
        tipo_vehiculo = options.get(request.form['tipo_vehiculo'], 0) 
        marca = request.form['marca']
        modelo= request.form['modelo']
        año= request.form['año']
        placa = request.form['placa']
        color =request.form['color']
        Datos = EntitiVehiculo(cedula, marca, tipo_vehiculo, modelo,año, placa, color)
        #dato=ModelCliente.Registrar(db,Datos )
        if not ModelCliente.buscarCliente(db, Datos.cedula) ==  None:
            if action == 'registrar':
                existe_vehiculo=ModelVehiculo.Buscar_Vehiculo(db,Datos.placa)
                if existe_vehiculo== None:
                    datos_completos= F.validar_datos(Datos)
                    if not datos_completos == False:
                        respuesta = ModelVehiculo.Registrar_Vehiculo(db,Datos)
                        if respuesta == True:
                            flash("Grabado con Exito")
                        else:
                            flash(f"Error al guardar: {respuesta}")
                    else:
                        flash(f"Faltaron Datos por llenar")
                else:
                    flash(f"Vehiculo ya existe")
            elif action == 'modificar':
                existe_vehiculo=ModelVehiculo.Buscar_Vehiculo(db,Datos.placa)
                if existe_vehiculo== None:
                    datos_completos= F.validar_datos(Datos)
                    if not datos_completos == False:
                        respuesta = ModelVehiculo.buscarCliente(db,Datos)
                        if respuesta == True:
                            respuesta = ModelVehiculo.Modificar_Vehiculo(db,Datos)
                            if respuesta == True:
                                flash(f"Modificado con Exito")
                            else:
                                flash(f"Error al guardar: {respuesta}")
                        else:
                            flash(f"Cliente no existe")
                    else:
                        flash(f"Faltaron Datos por llenar")
                else:
                    flash(f"Vehiculo ya existe")
        elif action == 'buscar':
            respuesta= ModelVehiculo.Buscar_Vehiculo(db,Datos.placa)
            print(respuesta)
            return render_template('Vehiculo.html', datos=respuesta )
        else:
            flash(f"Cliente no existe, debe registrarlo primero.")
    return render_template('Vehiculo.html')
@app.route('/servicios', methods=['GET', 'POST'])
@login_required
def servicios():
    if request.method == 'POST':
        action = request.form.get('action')  # Obtener la acción
        Fecha_Ingreso = request.form['Fecha_Ingreso']
        Fecha_Salida = request.form['Fecha_Salida']
        if Fecha_Salida == "" :
            Fecha_Salida = "20010101"

        placa= request.form['placa']
        Estado_Entrada= request.form['Estado_Entrada']
        Trabajo_Realizado = request.form['Trabajo_Realizado']
        Datos = EntitiServicios(Fecha_Ingreso, Fecha_Salida, placa, Estado_Entrada,Trabajo_Realizado)
        #dato=ModelCliente.Registrar(db,Datos )
        if not ModelVehiculo.Buscar_Vehiculo(db, Datos.placa) ==  None:
            if action == 'registrar':
                respuesta = ModelServicios.Registrar_Servicio(db,Datos)
                if respuesta == True:
                    flash("Grabado con Exito")
                else:
                    flash(f"Error al guardar{respuesta}")
            elif action == 'modificar':
                respuesta= ModelServicios.Modificar_Servicio(db,Datos)
                if respuesta == True:
                    flash("Modificado con Exito")
                elif respuesta == None :
                    flash("La placa no se encuentra Registrada")
                else:
                    flash(f"Error al guardar{respuesta}")
            elif action == 'buscar':
                respuesta= ModelServicios.Buscar_Servicio_Para_Id(db,Datos.placa)
                garantia = F.dias_de_garantia(respuesta[2])
                return render_template('servicios.html', datos=respuesta, garantia= garantia )
        else:
            flash(f"vehiculo no existe, debe registrarlo primero.")
    return render_template('servicios.html')
@app.route('/consultas', methods=['GET', 'POST'] )
@login_required
def Consultas():
    if request.method == 'POST': #Hay dos metodos el get que es cuando recien se entra, y el post, que es cuando se pide el login, aqui se hara la parte de cuando se esta pidiendo ese login
        cedula = request.form['Documento']
        respuesta = ModelCliente.buscarCliente(db,cedula)
        vehiculos = ModelVehiculo.Buscar_Vehiculo_por_cedula(db,cedula )
        return render_template('consultas.html', datos=respuesta, vehiculos= vehiculos )
    return render_template('consultas.html')
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