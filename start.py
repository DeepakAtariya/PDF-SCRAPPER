from flask import Flask,render_template,request
import server

app = Flask(__name__)

@app.route('/test',methods=['POST', 'GET'])
def hello_world():
    res = request.args['text']
    sug=server.getSuggestions(res)
    return sug 

@app.route('/start')
def start():
    return render_template('index.html',name="sample")

@app.route('/')
def start_server():
    # server.load()
    return "server is ready!"