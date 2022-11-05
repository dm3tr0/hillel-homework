from flask import Flask, request
import time, string
from random import choice

app = Flask(__name__)

@app.route('/whoami')

def whoami():
    return f'''
    {request.headers.get('User-Agent')}
    {request.remote_addr}
    {time.strftime('%H:%M:%S')}
    '''

@app.route('/sourse_code')

def sourse_code():
    file = open('main.py')
    text = str(file.read())
    return text

@app.route('/random')

def random():
    args = request.args
    specs = '!"№;%:?*()_+.'
    nums = '0123456789'
    dickt = {}
    dickt['l'] = int(args.get('length'))  # type: ignore
    dickt['s'] = int(args.get('specials'))  # type: ignore
    dickt['d'] = int(args.get('digits'))  # type: ignore
    if dickt['s'] == 0:
        specs = ''
    if dickt['d'] == 0:
        nums = ''   
    return f'''
    {''.join((choice(string.ascii_uppercase+specs+nums)) for _ in range(dickt['l']))}
    '''

app.run(debug=True)