from flask import Flask, redirect, url_for, request
app = Flask(__name__)

import socket
import subprocess
seed = 0

@app.route('/', methods = ['POST', 'GET'])
def seed_action():
    global seed
    if request.method == 'POST':
        subprocess.Popen("python3 stress_cpu.py", shell = True)
        return 'Good'
    elif request.method == 'GET':
        return socket.gethostname()


if __name__ == '__main__':
   app.run( host = '0.0.0.0', debug = False)
