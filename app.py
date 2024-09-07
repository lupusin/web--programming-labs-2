from flask import Flask,redirect,url_for
app = Flask(__name__)

@app.route("/")
@app.route("/index")
def start():
    return redirect("/menu",code=302)
@app.route("/lab1")
def lab1():
    return """
    <!doctype html?
    <html>
        <head>
            <title>Лапшин Егор Вячеславович, Лабороторная 1 </title>
        </head>
    <body>
        <header>
            НГТУ, ФБ, Лаборотрная работа 1
        </header>

        <h1>web-сервер на flask</h1>
        <div>
        Flask — фреймворк для создания веб-приложений на языке
        программирования Python, использующий набор инструментов
        Werkzeug, а также шаблонизатор Jinja2. Относится к категории так
        называемых микрофреймворков — минималистичных каркасов

        веб-приложений, сознательно предоставляющих лишь самые ба-
        зовые возможности.
        </div>
        <footer>
            &copy; Егор Лапшин , ФБИ-23, 3 курс, 2024
        </footer>
    </body>
    </html>
    """   
@app.route("/menu")
def menu():
    return """
    <!doctype html?
    <html>
        <head>
            <title>Лапшин Егор Вячеславович, Лабороторная 1 </title>
        </head>
    <body>
        <header>
            НГТУ, ФБ, Лаборотрная работа 1
        </header>

        <h1>НГТУ,ФБ, WEB-программирование, часть 2. Список лабораторных</h1>
        <div>
        <h2>Меню</h2>
        <li><a href="/lab1">Лабораторная 1</a></li>
        </div>
        <footer>
            &copy; Егор Лапшин , ФБИ-23, 3 курс, 2024
        </footer>
    </body>
    </html>"""

@app.route("/lab1/oak")
def oak():
    return '''
    <!doctype html>
    <header>'''+ url_for('static',filename='lab1.css') +'''</header>
    <html>
        <body>
            <h1>Дуб</h1>
            <img src="''' + url_for('static',filename='oak.jpg') + '''">
        </body>
    </html>
    '''  
    # ДОДЕЛАТЬ CSS