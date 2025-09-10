from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, this is a demo endpoint'


@app.route('/demoerror')
def demoerror():
    raise ValueError('A very specific bad thing happened.')
    #return 'This endpoint will throw an error'

if __name__ == '__main__':
    app.run(debug=True) 