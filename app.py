from flask import Flask, render_template, request
from suma import sumar

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    resultado = None
    if request.method == 'POST':
        a = int(request.form['a'])
        b = int(request.form['b'])
        resultado = sumar(a, b)
    return render_template('index.html', resultado=resultado)

if __name__ == '__main__':
    app.run(debug=True)
