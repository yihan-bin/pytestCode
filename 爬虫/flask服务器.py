from flask import Flask
import time

app = Flask(__name__)

@app.route('/bobo')
def indec_bobo():
    time.sleep(2)
    return 'Hellow Bobo'

@app.route('/jay')
def index_Jay():
    time.sleep(2)
    return 'Hellow Jay'
@app.route('/tom')
def index_tom():
    time.sleep(2)
    return 'Hellow Tom'

if __name__=='__main__':
    app.run(threaded = True)