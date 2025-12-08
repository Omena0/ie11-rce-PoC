from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return open('templates/index.html').read()

@app.route('/e')
def e():
    return open('templates/exploit.html').read()


app.run(debug=True)
