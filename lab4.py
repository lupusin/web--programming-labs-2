from flask import Blueprint,render_template,request, redirect
lab4 = Blueprint('lab4',__name__)


@lab4.route('/lab4/')
def lab():
    return render_template("lab4/lab4.html")

@lab4.route('/lab4/div-form')
def div_form():
    return render_template('lab4/div-form.html')

@lab4.route('/lab4/div', methods = ['POST'])
def div():
    x1 = request.form.get('x1')
    x2 = request.form.get('x2')
    if x1 == '' or x2 == '':
        return render_template('lab4/div-form.html', error='Оба поля должны быть заполнены!')
    try:
        x1 = int(x1)
        x2 = int(x2)
        if x2 == 0:
            return render_template('lab4/div-form.html', error='Деление на ноль невозможно', x1=x1, x2=x2)
        result = x1 / x2
        return render_template('lab4/div-form.html', x1=x1, x2=x2, result=result)
    except ValueError:
        return render_template('lab4/div-form.html', error='Оба поля должны содержать числа')

tree_count=0

MAX_TREES = 10
@lab4.route('/lab4/tree', methods = ['GET', 'POST'])
def tree():
    global tree_count
    if request.method == 'GET':
        return render_template('lab4/tree.html', tree_count=tree_count)
    
    operation = request.form.get('operation')

    if operation == 'cut':
        if tree_count > 0:
            tree_count -= 1
    elif operation == 'plant':
        if tree_count < MAX_TREES:
            tree_count += 1
    

    return redirect('/lab4/tree')