from flask import Flask, render_template

app = Flask(__name__)

# Randyr
@app.route('/')
def index_func():
    return render_template("index.html")

#Randyr
@app.route('/public/servicio')
def servicio_func():
    return render_template("public/servicio.html")

# Gustavo
@app.route('/public/mision_vision')
def mision_vision_func():
    return render_template("public/mision_vision.html")

# menu cliente # mockup 18
@app.route('/client/menu_cliente')
def menu_cliente_func():
    return render_template("client/menu_cliente.html")

# perfil cliente # mockup 19
@app.route('/client/perfil_cliente')
def perfil_cliente_func():
    return render_template("client/perfil_cliente.html")

# gestionar reserva # mockup 20
@app.route('/client/gestionar_reserva')
def gestionar_reserva_func():
    return render_template("client/gestionar_reserva.html")

# crear reserva # mockup 21
@app.route('/client/crear_reserva')
def crear_reserva_func():
    return render_template("client/crear_reserva.html")

# menu_administrador # mockup 6
@app.route('/admin/menu_administrador')
def menu_administrador_func():
    return render_template("admin/menu_administrador.html")

# perfil_administrador # mockup 7
@app.route('/admin/perfil_administrador')
def perfil_administrador_func():
    return render_template("admin/perfil_administrador.html")

# gestionar_usuarios # mockup 8
@app.route('/admin/gestionar_usuario')
def gestionar_usuarios_func():
    return render_template("admin/gestionar_usuarios.html")

# crear_usuario # mockup 9
@app.route('/admin/crear_usuario')
def crear_usuario_func():
    return render_template("admin/crear_usuario.html")

# lista_usuario # mockup 10
@app.route('/admin/lista_usuario')
def lista_usuario_func():
    return render_template("admin/lista_usuario.html")

# editar_usuario # mockup 11
@app.route('/admin/editar_usuario')
def editar_usuario_func():
    return render_template("admin/editar_usuario.html")

# gestionar_habitacion # mockup 12
@app.route('/admin/gestionar_habitacion')
def gestionar_habitacion_func():
    return render_template("admin/gestionar_habitacion.html")

# crear_habitacion # mockup 13
@app.route('/admin/crear_habitacion')
def crear_habitacion_func():
    return render_template("admin/crear_habitacion.html")

# listar_habitacion # mockup 14
@app.route('/admin/listar_habitacion')
def listar_habitacion_func():
    return render_template("admin/listar_habitacion.html")

# editar_habitacion # mockup 15
@app.route('/admin/editar_habitacion')
def editar_habitacion_func():
    return render_template("admin/editar_habitacion.html")

# gestionar_comentarios # mockup 16
@app.route('/admin/gestionar_comentarios')
def gestionar_comentarios_func():
    return render_template("admin/gestionar_comentarios.html")

# consultar_comentarios # mockup 17
@app.route('/admin/consultar_comentarios')
def consultar_comentarios_func():
    return render_template("admin/consultar_comentarios.html")

# Joanella
@app.route('/public/contacto')
def contacto_func():
    return render_template("public/contacto.html")


if __name__ == '__main__':
    app.run(host='localhost', port=8080,debug=True)
