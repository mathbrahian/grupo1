from flask import Flask, render_template

app = Flask(__name__)


@app.route('/inicio_route')
def inicio_func():
    return render_template("inicio.html")

if __name__ == '__main__':
    app.run(host='localhost', port=8080,debug=True)