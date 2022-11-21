import os
from flask import Flask, app, render_template
from flask_cors import CORS

app = Flask(__name__)

cors = CORS(app, resource={r"/*":{"origins": "*"}})

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/home')
def homePortfolio():
    return render_template('home.html')

@app.route('/sobre')
def about():
    return render_template('about.html')

@app.route('/portfolio')
def meuPortfolio():
    return render_template('portfolio.html')

@app.route('/contato')
def meuContato():
    return render_template('contato.html')

def main():
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)    

if __name__ == "__main__":
    main()