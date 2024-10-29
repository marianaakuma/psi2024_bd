from flask import Flask, render_template
import json
from flask import flash, redirect
from utils import db
import os
from flask_migrate import Migrate
from models.Usuario import Usuario

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
db_usuario = os.getenv('DB_USERNAME')
db_senha = os.getenv('DB_PASSWORD')
db_host = os.getenv('DB_HOST')
db_mydb = os.getenv('DB_DATABASE')

conexao = f"mysql+pymysql://{db_usuario}:{db_senha}@{db_host}/{db_mydb}"
app.config['SQLALCHEMY_DATABASE_URI'] = conexao
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app, db)

...
#codigo anterior o arquivo app.py

@app.route("/teste_insert")
def teste_insert():
    u = Usuario("mariana", "mariana@gmail.com", "123456")
    db.session.add(u)
    db.session.commit()
    return 'Dados inseridos com sucesso'

...
#codigo anterior o arquivo app.py

@app.route("/teste_delete")
def teste_delete():		
    u = Usuario.query.get(1)
    db.session.delete(u)
    db.session.commit()
    return 'Dados excluídos com sucesso'


@app.route("/teste_select")
def teste_select():
    u = Usuario.query.all()
    print(u)
    u = Usuario.query.get(1)
    return u.nome