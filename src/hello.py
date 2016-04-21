from flask import Flask, render_template, request, redirect
import thread, time
import RPi.GPIO as GPIO

## Select GPIO options
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

## Raspberry 2 GPIO pin numbers. 
pin_numbers = [3, 5, 7, 8, 10, 11, 13, 15, 16, 18, 19, 21, 22, 23, 24, 26]

## PWM frequncy
frequency = 50

## Setup pwm data structure. Keys are pins. Values
##  are tuple of (duty cycle value, pwm reference)  
def pwm_setup():
    pins = {}
    for pin_num in pin_numbers:
        GPIO.setup(pin_num, GPIO.OUT)
        pins[pin_num] = [0, GPIO.PWM(pin_num, frequency)]
        pins[pin_num][1].start(0)
    return(pins)

## Start setup
pins = pwm_setup()

## Define pwm update loop which will run in other thread
def pwm_loop():
    global pins
    while True:
        for pin in pins:
            pins[pin][1].ChangeDutyCycle(pins[pin][0])
        time.sleep(0.1)

## Start pwm loop
try:
    thread.start_new_thread(pwm_loop, ())
except:
    print 'Couldn\'t create second thread'
    exit()
    
## Define web server application with Flask
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def update_pwm():
    ## If POST, then update LED state
    if request.method == 'POST':
        ## Get new values from HTTP header
        index = int(request.form.get('Index'))
        brightness = int(request.form.get('Brightness'))

        ## Update the brightness
        pins[index][0] = brightness
        
        ## Redirect back to homepage
        return( redirect ('/') )

    ## If GET, then show homepage
    elif request.method == 'GET':
        return render_template('index.html')

## Run the program
if __name__ == '__main__':
    app.run('0.0.0.0')
