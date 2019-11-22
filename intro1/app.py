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

if __name__ == '__main__':
    
    gpio.setmode(gpio.BCM)
    gpio.setup(21, gpio.OUT)
    gpio.setup(12, gpio.OUT)
    gpio.setup(20, gpio.OUT)
    gpio.setup(18, gpio.OUT)
    
    
    app.run(debug=True ,host= '0.0.0.0' ,port=8080)
