from flask import Flask,redirect,url_for,render_template, session
import os
from flask_sqlalchemy import SQLAlchemy
from db import db
from lab1 import lab1
from lab2 import lab2
from lab3 import lab3
from lab4 import lab4
from lab5 import lab5
from lab6 import lab6
from lab7 import lab7
from lab8 import lab8
from lab9 import lab9
from dotenv import load_dotenv
from os import path
app = Flask(__name__)

app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY','cекрет')
app.config['DB_TYPE'] = os.getenv('DB_TYPE','postgres')

if app.config['DB_TYPE']=='postgres':
    db_name = 'postgres'
    db_user = 'egor_lapshin_orm'
    db_password = '123'
    host_ip = '127.0.0.1'
    host_port = 5432

    app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{db_user}:{db_password}@{host_ip}:{host_port}/{db_name}'

else:
    dir_path = path.dirname(path.realpath(__file__))
    db_path = path.join(dir_path,"egor_lapshin_orm.db")
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_path}'

db.init_app(app)

app.register_blueprint(lab1)
app.register_blueprint(lab2)
app.register_blueprint(lab3)
app.register_blueprint(lab4)
app.register_blueprint(lab5)
app.register_blueprint(lab6)
app.register_blueprint(lab7)
app.register_blueprint(lab8)
app.register_blueprint(lab9)
@app.route("/")
@app.route("/index")
def start():
    return redirect("/menu",code=302)


@app.route("/menu")
def menu():
    return '''
    <!doctype html>
    <link rel="stylesheet" href="'''+ url_for('static', filename='lab1.css')+ '''">
    <html>
        <head>
            <title>Лапшин Егор Вячеславович, Лабороторная 1 </title>
        </head>
    <body>
        <header>
            НГТУ, ФБ, Лабороторная работа 1
        </header>

        <h1>НГТУ,ФБ, WEB-программирование, часть 2. Список лабораторных</h1>
        <div>
        <h2>Меню</h2>
        <li><a href="/lab1">Лабораторная 1</a></li>
        <li><a href="/lab2">Лабораторная 2</a></li>
        <li><a href="/lab3">Лабораторная 3</a></li>
        <li><a href="/lab4">Лабораторная 4</a></li>
        <li><a href="/lab5">Лабораторная 5</a></li>
        <li><a href="/lab6">Лабораторная 6</a></li>
        <li><a href="/lab7">Лабораторная 7</a></li>
        <li><a href="/lab8">Лабораторная 8</a></li>
        <li><a href="/lab9">Лабораторная 9</a></li>
        </div>
        <footer>
            &copy; Егор Лапшин , ФБИ-23, 3 курс, 2024
        </footer>
    </body>
    </html>'''


