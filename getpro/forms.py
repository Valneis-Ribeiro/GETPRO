from flask_wtf import Form
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import EqualTo,Length,DataRequired

class FormLogin(Form):
    login = StringField('Login',validators=[DataRequired()])
    senha = PasswordField('Senha',validators=[DataRequired()])
    botao_login_submit = SubmitField('ENTRAR')

    