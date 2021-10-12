import os
from flask.helpers import flash
from flask import Flask, render_template, url_for, redirect, jsonify


app = Flask(__name__)

app.secret_key = os.urandom(24)

@app.route('/')
def inicio_func():
    return render_template("inicio.html")

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if(form.validate_on_submit()):
        usuario = form.usuario.data
        flash(f'Bienvenido(a), {usuario}')
        return redirect(url_for('index'))
    return render_template('login.html', form=form)

if __name__ == '__main__':
    app.run(host='localhost', port=8080,debug=True)
