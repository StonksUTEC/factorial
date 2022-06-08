from flask import Flask
app = Flask(__name__)



dp = [0 for i in range(100)]

@app.route('/')
def index():
    return "Hello"


def factorial(n):
    if dp[n] != 0:
        return dp[n]
    else:
        if n == 1 or n == 0:
            dp[n] = 1
        else:
            dp[n] = n*factorial(n-1)

        return dp[n]



@app.route('/factorial/<int:n>')
def print_factorial(n):
    temp = len(dp) - 1
    if n > len(dp):

        while temp < n:
            dp.append(0)
            temp = temp + 1 
    return f"Factorial is: {factorial(n)}"


@app.route('/<name>')
def my_view_func(name):

    return name


if __name__ == "__main__":
    app.run(debug=True)
