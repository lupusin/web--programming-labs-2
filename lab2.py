from flask import Blueprint,redirect,url_for,render_template
lab2 = Blueprint('lab2',__name__)


@lab2.route("/lab2/example")
def example():
    name='Егор Лапшин'
    group='ФБИ-23'
    kyrc='3'
    number=2
    fruits = [
        {'name':'яблоки','price':100},
        {'name':'груши','price':120},
        {'name':'апельсины','price':80},
        {'name':'мандарины','price':95},
        {'name':'манго','price':32}]
    books = [
        {'name':'Гроза','author':'Александр Островский','janr':'Пьеса','kolvo':'60'},
        {'name':'Морфий','author':'Михаил Булгаков','janr':'Русская классика','kolvo':'31'},
        {'name':'Капитанская дочка','author':'Александр Пушкин','janr':'Русская классика','kolvo':'130'},
        {'name':'Жена на один год','author':'Марья Коваленко','janr':'Роман','kolvo':'140'},
        {'name':'На дне','author':'Максим Горький','janr':'Пьеса','kolvo':'70'},
        {'name':'Скандал на драконьем факультете','author':'Тальяна Орлова','janr':'Любовное фентези','kolvo':'250'},
        {'name':'Братья Карамазовы','author':'Федор Достаевский','janr':'Русская классика','kolvo':'1140'},
        {'name':'Люди сороковой мили','author':'Джек Лондон','janr':'Рассказы','kolvo':'70'},
        {'name':'Искажающие реальность. Книга 1. Обратный отсчет','author':'Михаил Атаманов','janr':'Боевая фантастика','kolvo':'392'},
        {'name':'Граф Монте-Кристо','author':'Александр Дюма','janr':'Исторические приключения','kolvo':'1500'}
    ]
    return render_template('example.html',group=group,kyrc=kyrc,number=number,name=name,fruits=fruits,books=books)


@lab2.route('/lab2/')
def labb():
    return render_template('lab2/lab2.html')


@lab2.route('/lab2/cars')
def cars():
    return render_template('lab2/cars.html')