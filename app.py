from flask import Flask,redirect,url_for,render_template
from lab1 import lab1
from lab2 import lab2


app = Flask(__name__)
app.register_blueprint(lab1)
app.register_blueprint(lab2)

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
        </div>
        <footer>
            &copy; Егор Лапшин , ФБИ-23, 3 курс, 2024
        </footer>
    </body>
    </html>'''


