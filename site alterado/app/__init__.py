from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('pag miceli.html')
@app.route('/login')
def login():
    nome = request.form("user")
    senha = request.form("senha")
    arq = open('/cadastros.txt','r')
    texto = open.read()
    if '%s' %nome +' %s' %senha in texto:
        return render_template('pag miceli.html')
    else:
        return render_template('pag miceli.html')


if __name__ == '__main__':
    app.run(debug = True)
