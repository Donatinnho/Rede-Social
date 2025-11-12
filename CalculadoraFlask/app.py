from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.secret_key = 'super secret key'

@app.route('/', methods=['GET','POST'])
def calculadora():
    resultado = None

    if request.method == 'POST':
        num1 = request.form.get('num1')
        num2 = request.form.get('num2')

        if num1 == "" or num2 == "":
            resultado = 'Numero invalido'
            flash(resultado)
        else:
            resultado = float(num1) + float(num2)
            flash(resultado)

    return render_template('calculadora.html', resultado=resultado)

if __name__ == '__main__':
    app.run(debug=True)
