from flask import Flask, render_template, request
from .suma import sumar

def create_app():
    app = Flask(__name__)

    @app.route('/', methods=['GET', 'POST'])
    def index():
        resultado = None
        if request.method == 'POST':
            try:
                a = int(request.form['a'])
                b = int(request.form['b'])
                resultado = sumar(a, b)
            except (ValueError, TypeError):
                resultado = "Error: Ingrese números válidos"
        return render_template('index.html', resultado=resultado)

    return app
