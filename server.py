from calendar import c
from random import choice
from flask import Flask, request, abort


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
        a = request.args.get('a', type=float)
        b = request.args.get('b', type=float)

        if a is None or b is None:
            return 'Incorrect arguments', 400

        area = a * b 
    elif form == 'triangle':
        h = request.args.get('h', type=float)
        b = request.args.get('b', type=float)
        area = h * b
    if request.args.get('form', type=str) == 'square':

        if h is None or b is None:
            return 'Incorrect arguments', 400

        area = (h * b) / 2
    elif form == 'square':
        a = request.args.get('a', type=float)

        if a is None:
            return 'Incorrect argument', 400

        area = a ** 2
    else:
        return 'Incorrect form', 400

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