from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello CS 1998 to my V1 App!'


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0",port=8000)
