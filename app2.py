
from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/hello', methods=['GET'])
def say_hello():
    name = request.args.get("name", "") # tutaj leci str
    title = request.args.get("title", "")
    if name:
        resp = f"Hello {title} {name}" if title else f"Hello {name}"
    else:
        resp = f"Hello {title}" if title else "Hello"
    return resp

if __name__ == '__main__':
    app.run(port=5005)
