import json

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('web/giris.html')

@app.route('/veri')
def veri():
    return json.dumps({'veri': 'bu bir veridir'})

if __name__ == '__main__':
    app.run(debug=True)