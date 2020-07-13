from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')

def index():
    return render_template('index.html', list = ["アイテム１","アイテム２","アイテム３"])

if __name__=='__main__':
    app.debug = True
    app.run()