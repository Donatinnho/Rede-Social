from flask import Flask, render_template, request, redirect, url_for, session, flash

app = Flask(__name__)
app.secret_key = 'secret_key'

USERNAME = 'admin'
PASSWORD = '1234'

@app.route('/')
def home():
    if "username" in session:
        return render_template('home.html', username=session['username'])
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
         username = request.form['username']
         password = request.form['password']
         if username == USERNAME and password == PASSWORD:
             session['username'] = username
             flash('Login realizado com sucesso!', 'success')
             return redirect(url_for('home'))
         else:
             flash("Credenciais inválidas!", "danger")

    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    flash('Logout realizado com sucesso!', 'warning')
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)