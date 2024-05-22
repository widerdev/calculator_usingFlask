from flask import Flask,request,render_template

app = Flask(__name__)  # This (app) is the object


@app.route('/')
def welcome():
    return "Welcome to Flask"

app.route('/cal', methodds=["GET"])
def math_operation():
    operation= request.json["operation"]
    number1 = request.json["number1"]
    number2 = request.json["number2"]

    if operation== "add":
        result = number1+number2
    elif operation == "multiply":
        result = number1*number2
    elif operation == "division":
        result= number1/number2
    elif operation== "subtract":
        result = number1-number2
    else:
        return "invalid input"
    return result



print(__name__)
if __name__ == "__main__":
    app.run()

