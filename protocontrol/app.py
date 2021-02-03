from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
def test():
    return render_template('images.html')


@app.route('/hello')
def hello():
    return "Hello"


if __name__ == '__main__':
    app.run()
