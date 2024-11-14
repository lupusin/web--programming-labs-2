from flask import Flask,redirect,url_for,render_template, session

from lab1 import lab1
from lab2 import lab2
from lab3 import lab3
from lab4 import lab4
from lab5 import lab5

app = Flask(__name__)

app.secret_key = 'secret'
app.register_blueprint(lab1)
app.register_blueprint(lab2)
app.register_blueprint(lab3)
app.register_blueprint(lab4)
app.register_blueprint(lab5)
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
        </div>
        <footer>
            &copy; Егор Лапшин , ФБИ-23, 3 курс, 2024
        </footer>
    </body>
    </html>'''


