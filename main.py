from flask import Flask, render_template

app = Flask(__name__)

# Randyr
@app.route('/')
def inicio_func():
    return render_template("inicio.html")

#Randyr
@app.route('/servicio')
def servicio_func():
    return render_template("servicio.html")

# Gustavo
@app.route('/mision_vision')
def mision_vision_func():
    return render_template("mision_vision.html")

# Joanella
@app.route('/contacto')
def contacto_func():
    return render_template("contacto.html")


if __name__ == '__main__':
    app.run(host='localhost', port=8080,debug=True)
