from flask import Flask

app = Flask(__name__)

@app.route('/thing')
def hello():
    return '<h1>Hello, World!</h1>'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
