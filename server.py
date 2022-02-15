from calendar import c
from random import choice
from flask import Flask, request, abort, render_template
from figures import Figure, Square, Triangle, Rectangle
import logging

app = Flask(__name__, static_url_path='/static')

# status codes
# 2xx - successful, 200 - OK, 201 - Created
# 3xx - redirect, 301 - Permanent, 302 - Temporary
# 4xx - client error, 400 - Bad Request, 401 - Unauthorized, 403 - Forbidden, 404 - Not Found
# 5xx - server error, 500 - Internal Server Error

# 10 + 5 + 16 = 31
summ = 0

# query - ?a=1&b=2 GET / DELETE, не имеют тела
# x-www-form-urlencoded - передача в body, содержимое a=1&b=2 POST, PUT
# multipart/form-data - передача файлов
# json в body 
# JSON - JavaScript Object Notation
# {
#     "field": "value",
#     "field2": 25,
#     "field3": -25.04,
#     "field4": true,
#     "field5": null,
#     "field6": {
#         "field7": "aaa"
#     },
#     "field8":  [{"a": 2}, {"b": 3}]
# }

# GET - получить информацию 
# POST - добавить новую информацию
# PUT - изменить старую информацию
# DELETE - удалить что-либо

# HTML + CSS + JavaScript
# HTML - структура документа
# CSS - каскадная таблица стилей, оформление документа, стилизация
# JS - программирование, анимация, игры, рисование, любое программное взаимодействие с сервером

# red green blue - от 0 до 255

# ДЗ  - сделать форму на сайте для взаимодействия с калькулятором

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/figures')
def about():
    return render_template('figures.html')

@app.route("/area")
def get_sqarea():
    form = request.args.get('form', type=str)
    if form == 'rectangle':
        if request.args.get('a', type=float) is None and request.args.get('b', type=float) is None:
            return 'Incorrect arguments', 400
        rectangle = Rectangle(width=request.args.get('a', type=float), length=request.args.get('b', type=float))
        area = rectangle.get_area()
    
    elif form == 'triangle':
        if request.args.get('b', type=float) is None and request.args.get('h', type=float) is None:
            return 'Incorrect arguments', 400 
        triangle = Triangle(basis=request.args.get('b', type=float), height=request.args.get('h', type=float))
        area = triangle.get_area()
    
    elif form == 'square':
        if request.args.get('a', type=float) is None:
            return 'Incorrect arguments', 400 
        square = Square(side=request.args.get('a', type=float))
        area = square.get_area()
    
    else:
        return "incorrect form", 400
    

    global summ
    summ += area

    return 'Result {} squre meters'.format(area)


@app.route('/sum')
def get_sum():
    global summ
    return str(summ)

@app.route('/sum', methods=['DELETE'])
def delete_sum():
    global summ
    summ = 0

    return 'Sum has been cleared'


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8080) 