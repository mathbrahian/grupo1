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
@app.route('/public/menu_cliente')
def menu_cliente_func():
    return render_template("public/menu_cliente.html")

# perfil cliente # mockup 19
@app.route('/public/perfil_cliente')
def perfil_cliente_func():
    return render_template("public/perfil_cliente.html")

# gestionar reserva # mockup 20
@app.route('/public/gestionar_reserva')
def gestionar_reserva_func():
    return render_template("public/gestionar_reserva.html")

# crear reserva # mockup 21
@app.route('/public/crear_reserva')
def crear_reserva_func():
    return render_template("public/crear_reserva.html")

# Joanella
@app.route('/public/contacto')
def contacto_func():
    return render_template("public/contacto.html")


if __name__ == '__main__':
    app.run(host='localhost', port=8080,debug=True)
