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

# Joanella
@app.route('/public/contacto')
def contacto_func():
    return render_template("public/contacto.html")


if __name__ == '__main__':
    app.run(host='localhost', port=8080,debug=True)
