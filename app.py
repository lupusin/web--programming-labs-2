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
        <li><a href="/menu">меню</a></li>
        <h2>Реализованные роуты</h2>
        <li><a href="/lab1/oak">/lab1/oak - дуб</a></li>
        <li><a href="/lab1/python">/lab1/python - питон</a></li>
        <li><a href="/lab1/film">/lab1/film - фильм</a></li>
        <footer>
            &copy; Егор Лапшин , ФБИ-23, 3 курс, 2024
        </footer>
    </body>
    </html>
    """   
@app.route("/menu")
def menu():
    return '''
    <!doctype html?
    <link rel="stylesheet" href="'''+ url_for('static', filename='lab1.css')+ '''">
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
    </html>'''

@app.route("/lab1/oak")
def oak():
    return '''
    <!doctype html>
    <link rel="stylesheet" href="'''+ url_for('static', filename='lab1.css')+ '''">
    <header>
    </header>
    <html>
        <body>
            <h1>Дуб</h1>
            <div>
            <h3>На краю дороги стоял старый одинокий дуб.
             Крепко стоял, надёжно. Не страшны ему были ни сильные порывы ветра, ни хлёсткие ливни, ни вьюжные метели.
             </h3>
            </div>
            <div>
            <img src="''' + url_for('static',filename='oak.jpg') + '''">
            </div>
        </body>
    </html>
    '''  
@app.route("/lab1/student")
def student():
        return '''
    <!doctype html?
    <html>
    <link rel="stylesheet" href="'''+ url_for('static', filename='lab1.css')+ '''">
        <head>
            <title>Лапшин Егор Вячеславович, Лабороторная 1 </title>
        </head>
    <body>
        <header>
            НГТУ, ФБ, Лаборотрная работа 1
        </header>

        <h1>Лапшин Егор Вячеславович</h1>
        <div>
        <img src="''' + url_for('static',filename='mda.png') + '''">
        </div>
        <footer>
            &copy; Егор Лапшин , ФБИ-23, 3 курс, 2024
        </footer>
    </body>
    </html>'''

@app.route("/lab1/python")
def python():
    return '''
    <!doctype html?
    <html>
    <link rel="stylesheet" href="'''+ url_for('static', filename='lab1.css')+ '''">
        <head>
            <title>Лапшин Егор Вячеславович, Лабороторная 1 </title>
        </head>
    <body>
        <header>
            НГТУ, ФБ, Лаборотрная работа 1
        </header>

        <h1>Язык программирования Python</h1>
    
    <h2>Описание</h2>
    <p>Python (МФА: [ˈpʌɪθ(ə)n]; в русском языке встречаются названия пито́н[12] или па́йтон[13]) — мультипарадигмальный высокоуровневый язык программирования общего назначения с динамической строгой типизацией и автоматическим управлением памятью[14][15], ориентированный на повышение производительности разработчика, читаемости кода и его качества, а также на обеспечение переносимости написанных на нём программ[16]. Язык является полностью объектно-ориентированным в том плане, что всё является объектами[14]. Необычной особенностью языка является выделение блоков кода отступами[17]. Синтаксис ядра языка минималистичен, за счёт чего на практике редко возникает необходимость обращаться к документации[16]. Сам же язык известен как интерпретируемый и используется в том числе для написания скриптов[14]. Недостатками языка являются зачастую более низкая скорость работы и более высокое потребление памяти написанных на нём программ по сравнению с аналогичным кодом, написанным на компилируемых языках, таких как C или C++[14][16].</p>


    <h2>Архитектурные черты</h2>
    <ul>
        <li>Динамическая типизация</li>
        <li>Автоматическое управление памятью</li>
        <li>Полная интроспекция</li>
        <li>Механизм обработки исключений</li>
        <li>Поддержка многопоточных вычислений с глобальной блокировкой интерпретатора (GIL)</li>
        <li>Высокоуровневые структуры данных</li>
        <li>Разбиение программ на модули и пакеты</li>
    </ul>

    <h2>История разработки</h2>
    <p>Разработка языка ведётся через предложения по расширению языка PEP (англ. Python Enhancement Proposal), в которых описываются нововведения, делаются корректировки согласно обратной связи от сообщества и документируются итоговые решения. Срок поддержки версии Python 2 закончился в 2020 году. На текущий момент активно развивается версия языка Python 3.</p>

        <img src="''' + url_for('static',filename='python.jpg') + '''">
        </div>
        <footer>
            &copy; Егор Лапшин , ФБИ-23, 3 курс, 2024
        </footer>
    </body>
    </html>'''
@app.route("/lab1/film")
def film():
    return '''
    <!doctype html?
    <html>
    <link rel="stylesheet" href="'''+ url_for('static', filename='lab1.css')+ '''">
        <head>
            <title>Лапшин Егор Вячеславович, Лабороторная 1 </title>
        </head>
    <body>
        <header>
            НГТУ, ФБ, Лаборотрная работа 1
        </header>
</head>
<body>
    <h1>Фильм "Гордость и предубеждение"</h1>
    
    <h2>Описание</h2>
    <p>"Гордость и предубеждение" – это историко-романтический драматический фильм 2005 года, снятый Джо Райтом в его полнометражном режиссерском дебюте и основанный на романе 1813 года Джейн Остин. В фильме рассказывается о пяти сестрах из английской семьи помещиков, которые занимаются вопросами брака, морали и заблуждений. Кира Найтли играет Элизабет Беннет, в то время как Мэтью Макфейден играет мистера Дарси, который влюбляется в нее.</p>

    <h2>Создатели фильма</h2>
    <ul>
        <li>Дебора Моггач – сценарист</li>
        <li>Джо Райт – режиссер</li>
    </ul>

    <h2>Актеры</h2>
    <ul>
        <li>Кира Найтли – Элизабет Беннет</li>
        <li>Мэтью Макфейден – мистер Дарси</li>
    </ul>

    <h2>Производство</h2>
    <p>Фильм был произведен Working Title Films совместно с StudioCanal и выпущен 16 сентября 2005 года в Соединенном Королевстве и 11 ноября в Соединенных Штатах. Темами фильма подчеркивают реализм, романтизм и семью.</p>

    <h2>Отзывы и критика</h2>
    <p>Ученые Остин высказали мнение, что работа Райта создала новый гибридный жанр, смешав традиционные черты фильма о наследии с "техниками кинопроизводства, ориентированными на молодежь".</p>

        <img src="''' + url_for('static',filename='film.png') + '''">
        </div>
        <footer>
            &copy; Егор Лапшин , ФБИ-23, 3 курс, 2024
        </footer>
    </body>
    </html>'''