from flask import Flask
from flask import render_template,request
from flaskext.mysql import MySQL
from datetime import datetime

app = Flask(__name__)
mysql = MySQL()
app.config['MYSQL_DATABASE_HOST']='localhost'
app.config['MYSQL_DATABASE_USER']='root'#si no lo cambié es el que viene por defecto
app.config['MYSQL_DATABASE_PASSWORD']=''#no usamos ninguno ahora
app.config['MYSQL_DATABASE_BD']='bd_tp1'
mysql.init_app(app)

if __name__ == '__main__':
    app.run(debug=True)

@app.route('/')
def index():
    return render_template('clientes/index.html')

@app.route('/Quienes_somos')
def quienes_somos():
    return render_template('clientes/Quienes_somos.html')

@app.route('/Servicios')
def servicios():
    return render_template('clientes/Servicios.html')

@app.route('/Contacto')
def Contacto():
    return render_template('clientes/Contacto.html')

@app.route('/store', methods=['POST'])
def storage():
    _nombre = request.form["nombre"]
    _apellido = request.form["apellido"]
    _celular = request.form["telefono"]
    _mail = request.form["email"]
    _zona  = request.form["zona"]
    _descripcion  = request.form["comentarios"]
    _foto  = request.files['foto']

    now=datetime.now()#con esto trae el horario hasta en microsegundos
    tiempo = now.strftime("%Y%H%M%S")#nos permite convertir a cadena esa fecha en años hora min y seg
    #pregunto si el nombre de la foto no esta vacio
    if _foto.filename != '':
        nuevoNombreFoto=tiempo+_foto.filename #concateno el tiempo con el nombre e la foto "filename"
        _foto.save("uploads/"+nuevoNombreFoto)#permite guardar el archivo en el lugar que quiero almacenarlo
    sql = "INSERT INTO `bd_tp1`.`clientes` (`id`, `nombre`, `apellido`, `celular`, `mail`, `zona`, `descripcion`, `foto`) VALUES (NULL, %s, %s, %s, %s, %s, %s, %s);" #variable para instrucción de sql
    datos=(_nombre,_apellido,_celular,_mail,_zona,_descripcion,nuevoNombreFoto)#Tupla que almacena los datos
    conn = mysql.connect() #metodo propio de mysql que conecta con la base de datos
    cursor = conn.cursor() #para procesar la fila que devuelve el sistema (almacena lo que ejecuta)
    cursor.execute(sql,datos) #le paso la instrucción o la escribo directamente
    conn.commit() #para que los cambios se vean reflejados en la base de datos
    return render_template('clientes/Contacto.html')

