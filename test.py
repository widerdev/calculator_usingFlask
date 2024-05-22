from flask import Flask,request,render_template

app = Flask(__name__)  # This (app) is the object


@app.route('/')
def welcome():
    return "Welcome to Flask"




print(__name__)
if __name__ == "__main__":
    app.run()

