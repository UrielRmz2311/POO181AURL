
# Importacion de framework -------------------------------------------
from flask import Flask,render_template,request,redirect,url_for,flash
# Importacion de MySQL con FLASK
from flask_mysqldb import MySQL

# Inicialización del APP ó servidor ----------------------------------
app= Flask(__name__)

# Conexion de la base de datos ---------------------------------------
app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root' # Usuario de MySQL 
app.config['MYSQL_PASSWORD']=''  # Contraseña MySQL
app.config['MYSQL_DB']='db_floreria'  # Nombre de la base de datos
app.secret_key='mysecretkey'
mysql= MySQL(app)

# Declaración de las rutas hhtp://localhost:5000 ---------------------

  # Ruta principal -------------
@app.route('/')
def fruteria():
    return render_template('index.html')

# ruta http:localhost:500/guardar tipo POST para Insert
@app.route('/guardar', methods=['POST'] )
def guardar():
    if request.method == 'POST':
    #Pasamos a variables el contenido de los input
        Varflor= request.form['txtflor']
        Varcant= request.form['txtcantidad']
        Varprecio= request.form['txtprecio']
        print(Varflor,Varcant,Varprecio)
        
        #Conectar y ejecutar el insert
        CS = mysql.connection.cursor()
        CS.execute('insert into tbflores(Nombre,cantidad,precio) values (%s,%s,%s)',(Varflor,Varcant,Varprecio))
        mysql.connection.commit()
    flash('La flor se registro correctamente')
    return render_template('index.html')

@app.route('/eliminar/<id>')
def borrar(id):
    cursorId = mysql.connection.cursor()
    cursorId.execute('select * from tbflores where id= %s',(id,))
    consulId = cursorId.fetchone()
    return render_template('eliminar.html', flor = consulId)

@app.route('/borrar/<id>', methods=['POST'])
def eliminar(id):
    if request.method == 'POST':

        cursorAct = mysql.connection.cursor()
        cursorAct.execute('delete from tbflores where id= %s',(id,))
        mysql.connection.commit()
        
    flash('Se elimino la flor correctamente')
    return redirect(url_for('consulta'))

@app.route('/Consulta')
def consulta():
    CC= mysql.connection.cursor()
    CC.execute('select * from tbflores')
    conflor= CC.fetchall()
    print(conflor)
    return render_template('consulta.html', listaflor = conflor)


# Ejecución de Servidor en el Puerto 5100 ---------------------------- 
if __name__ == '__main__':
    app.run(port=5200,debug=True)
    