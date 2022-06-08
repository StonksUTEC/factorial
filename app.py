
from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return "Hello"


@app.route('/factorial/<int:n>')
def factorial(n):
    result = 1
    for i in range(1,n+1):
    	result *= i
    return f"Factorial is: {result}"

@app.route('/<name>')
def my_view_func(name):
    return name

if __name__ == "__main__":
    app.run(debug=True)
