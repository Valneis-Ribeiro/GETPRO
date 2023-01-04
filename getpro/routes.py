from getpro import app
from flask import render_template,url_for
from getpro.forms import FormLogin


# Página de login
# ------------- Em desenvolvimento
@app.route('/',methods=['GET','POST'])
def login():
    form_login = FormLogin()
    return render_template('login.html',form_login=form_login)


# Página de lançamentos de operacionais
@app.route('/lancamentos', methods=['GET','POST'])
def lancamentos_():
    return render_template('lancamentos.html')


# Página de ocorrencias
@app.route('/ocorrencias', methods=['GET','POST'])
def ocorrencias():
    return render_template('ocorrencias.html')


# Página de ranking Geral
@app.route('/ranking-geral', methods=['GET','POST'])
def ranking_geral():
    return render_template('rankingGeral.html')


# Sair da página
@app.route('/sair', methods=['GET','POST'])
def sair():
    pass





