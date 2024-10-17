from flask import Blueprint,redirect,url_for,render_template,request, make_response
lab3 = Blueprint('lab3',__name__)

@lab3.route('/lab3/')
def lab():
    name = request.cookies.get('name')
    if name==None:
        name = " Геральд"
    name_color = request.cookies.get('name_color')
    age = request.cookies.get('age')
    if age==None:
        age = " неизвестно"
    return render_template('lab3/lab3.html',name=name,name_color=name_color,age=age)


@lab3.route('/lab3/cookie')
def cookie():
    resp=make_response(redirect('/lab3/'))
    resp.set_cookie('name','Alex',max_age=5 )
    resp.set_cookie('age','20')
    resp.set_cookie('name_color','magenta')
    return resp


@lab3.route('/lab3/del_cookie')
def del_cookie():
    resp=make_response(redirect('/lab3/'))
    resp.delete_cookie('name')
    resp.delete_cookie('age')
    resp.delete_cookie('name_color')
    resp.delete_cookie('color')
    return resp


@lab3.route('/lab3/form1')
def form1():
    errors={}
    user =request.args.get('user')
    if user=="":
        errors['user'] = 'Заполните поле!'
    age =request.args.get('age')
    if age=="":
        errors['user'] = 'Заполните поле!'
    sex = request.args.get('sex')
    return render_template('lab3/form1.html',user=user,age=age,sex=sex, errors=errors)


@lab3.route('/lab3/order')
def order():
    return render_template('lab3/orders.html')

@lab3.route('/lab3/pay')
def pay():
    global price
    price=0
    drink = request.args.get('drink')
    if drink== 'cofee':
        price=120
    elif drink== 'black-tea':
        price = 80
    else:
        price=70
    if request.args.get('milk')=='on':
        price+=30
    else:
        pass
    if request.args.get('sugar')=='on':
        price+=10
    else:
        pass
    return render_template('lab3/pay.html',price=price)


@lab3.route('/lab3/success')
def success():
    global price
    return render_template('lab3/success.html',price=price)


@lab3.route('/lab3/settings')
def settings():
    color=request.args.get('color')
    if color:
        resp = make_response(render_template('lab3/settings.html'))
        resp.set_cookie('color',color)
        return resp
    color=request.cookies.get('color')
    resp = make_response(render_template('lab3/settings.html',color=color))
    return resp


@lab3.route('/lab3/ticket_form')
def ticket():
    return render_template('lab3/ticket_form.html')

@lab3.route('/lab3/calculate', methods=['POST'])
def calculate():
    fio = request.form['fio']
    shelf = request.form['shelf']
    bedding = 'bedding' in request.form
    luggage = 'luggage' in request.form
    age = int(request.form['age'])
    departure = request.form['departure']
    destination = request.form['destination']
    date = request.form['date']
    insurance = 'insurance' in request.form

    # Цены и расчеты
    price = 700 if age < 18 else 1000

    if shelf in ['lower', 'lower_side']:
        price += 100
    if bedding:
        price += 75
    if luggage:
        price += 250
    if insurance:
        price += 150

    ticket_info = {
        'fio': fio,
        'shelf': shelf,
        'bedding': bedding,
        'luggage': luggage,
        'age': age,
        'departure': departure,
        'destination': destination,
        'date': date,
        'insurance': insurance,
        'price': price,
        'child_ticket': age < 18
    }

    return render_template('lab3/ticket.html', ticket=ticket_info)


books = [
    {"title": "Мастер и Маргарита", "price": 500, "author": "Михаил Булгаков", "genre": "Роман"},
    {"title": "1984", "price": 750, "author": "Джордж Оруэлл", "genre": "Фантастика"},
    {"title": "Преступление и наказание", "price": 1200, "author": "Федор Достоевский", "genre": "Роман"},
    {"title": "Война и мир", "price": 1500, "author": "Лев Толстой", "genre": "Исторический роман"},
    {"title": "Трудно быть богом", "price": 600, "author": "Аркадий и Борис Стругацкие", "genre": "Научная фантастика"},
    {"title": "Собачье сердце", "price": 400, "author": "Михаил Булгаков", "genre": "Проза"},
    {"title": "451 градус по Фаренгейту", "price": 800, "author": "Рэй Брэдбери", "genre": "Фантастика"},
    {"title": "Гарри Поттер и философский камень", "price": 900, "author": "Дж.К. Роулинг", "genre": "Фэнтези"},
    {"title": "Анна Каренина", "price": 1500, "author": "Лев Толстой", "genre": "Роман"},
    {"title": "Шум и ярость", "price": 1200, "author": "Уильям Фолкнер", "genre": "Роман"},
    {"title": "Убить пересмешника", "price": 600, "author": "Харпер Ли", "genre": "Роман"},
    {"title": "Девочка с пилами", "price": 350, "author": "Рей Бредбери", "genre": "Фантастика"},
    {"title": "Принцесса Монако", "price": 900, "author": "Моника Мерчези", "genre": "Роман"},
    {"title": "Дюна", "price": 1300, "author": "Фрэнк Герберт", "genre": "Научная фантастика"},
    {"title": "Степной волк", "price": 700, "author": "Герман Гессе", "genre": "Роман"},
    {"title": "В поисках утра", "price": 850, "author": "Николай Гоголь", "genre": "Проза"},
    {"title": "История одного города", "price": 400, "author": "Михаил Салтыков-Щедрин", "genre": "Сатира"},
    {"title": "Гордость и предубеждение", "price": 550, "author": "Джейн Остин", "genre": "Роман"},
    {"title": "Цветы для Элджернона", "price": 700, "author": "Дэниел Киз", "genre": "Научная фантастика"},
    {"title": "Крысолов", "price": 800, "author": "Фрэнсис Бёрнетт", "genre": "Проза"},
    {"title": "Сияние", "price": 950, "author": "Стивен Кинг", "genre": "Ужасы"},
]

@lab3.route('/lab3/search_form')
def search_form():
    return render_template('lab3/search_form.html')

@lab3.route('/lab3/results', methods=['POST'])
def search_results():
    min_price = request.form['min_price']
    max_price = request.form['max_price']

    # Фильтруем книги по ценам
    filtered_books = [
        book for book in books
        if (int(min_price) <= book['price'] <= int(max_price))
    ]

    return render_template('lab3/search_results.html', books=filtered_books)