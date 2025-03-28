from flask import Flask

app = Flask(__name__)

@app.route('/hello')
def say_hello():
    return "Hello World"

@app.route('/')
def say_he():
    return "Hello z innej strony"

@app.route('/test')
def say():
    return "test"

if __name__ == '__main__':
    app.run()
