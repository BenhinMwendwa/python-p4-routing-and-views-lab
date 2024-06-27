from flask import Flask
app= Flask(__name__)
 
@app.route('/')
def index():
     return "<h1>Python Operations with Flask Routing and Views</h1>"
 
@app.route('/print/string:param>')
def print_string(param):
    print(param) #print to console
    return f'<h1> Printed String:{param}</h1>'
@app.route('/count/<int:param>')
def count(param):
    for i in range(int(param)+1):
        print(i) #print to console
    return '<h1>Counted Integer: 0-'+param+'</h1>'
@app.route('/math/integer:num1/operation/integer:num2/')
def math(num1,operation,num2):
    result =None
    if operation =='add':
        result = int(num1) + int(num2)
    elif operation =='subtract':
        result = int(num1) - int(num2)
    elif operation =='multiply':
        result = int(num1) * int(num2)
    elif operation =='divide':
        if int(num2) !=0:
          result = int(num1) / int(num2)
        else:
            return '<h1>Error: Division by zero!</h1>'
    else:
        return '<h1>Error: Invalid operation! Choose add, subtract, multiply, or divide.</h1>'

    return f'<h1>Math Operation: {num1} {operation} {num2} = {result}</h1>'

if __name__ == '__main__':
    app.run(debug=True) 


