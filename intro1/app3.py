#from flask import Flask, render_template

#app = Flask(__name__)

#@app.route('/')
#def index():
 #   return render_template('index.html')


#if __name__ == "__main__":
  #  app.run(debug=True)
from flask import Flask, render_template, request
import RPi.GPIO as gpio
import time
import socket
import threading



app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    print(request)
    print(request.form)
    if request.method == 'POST':
        if 't1' in request.form:
            print('Bringing down Target 1')
            gpio.output(20, 1)
            time.sleep(3)
            gpio.output(20, 0)
        elif 't2' in request.form:
            print('Bringing down Target 2')
            gpio.output(21, 1)
            time.sleep(3)
            gpio.output(21, 0)
            clientsocket, adress = s.accept()
            clientsocket.send(bytes("thank god this works", "utf-8"))
        elif 't3' in request.form:
            print('Bringing down Target 3')
            gpio.output(12, 1)
            time.sleep(3)
            gpio.output(12, 0)
        elif 't4' in request.form:
            print('Bringing down Target 4')
            gpio.output(18, 1)
            time.sleep(3)
            gpio.output(18, 0)
        return render_template('index.html', text='My Text')
    else:
        return render_template('index.html', text='My Text')
def webserver():
        app.run(debug=True ,host= '0.0.0.0' ,port=5500, use_reloader = False)
        
def server():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((socket.gethostname(), 1234))
    s.listen(5)

    while True:
        clientsocket, adress = s.accept()
        print("connection from {adress} has been established!")
        clientsocket.send(bytes("welcome to the server", "utf-8"))
    

if __name__ == '__main__':
    
    x = threading.Thread(target = server, daemon = True)
    x2 = threading.Thread(target = webserver, daemon = True)
    x2.start()
    x.start()
    
    gpio.setmode(gpio.BCM)
    gpio.setup(21, gpio.OUT)
    gpio.setup(12, gpio.OUT)
    gpio.setup(20, gpio.OUT)
    gpio.setup(18, gpio.OUT)
    
    
