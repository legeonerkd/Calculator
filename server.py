from calendar import c
from random import choice
from flask import Flask, request, abort
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

    return ''


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8080) 