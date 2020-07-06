from flask import Flask
import datetime
import calendar

app = Flask(__name__)

@app.route('/')

def hello_world():
    mdhm1 = datetime.datetime.now()
    MDHM2 = mdhm1.strftime('%m/%d %H:%M')
    return MDHM2

if __name__=='__main__':
    app.debug = True
    app.run()