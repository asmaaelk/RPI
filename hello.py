from flask import Flask, render_template, request, redirect
import thread, time
#import RPi.GPIO as GPIO

# GPIO.setmode(GPIO.BOARD)
# GPIO.setwarnings(False)

## Raspberry 2 GPIO pin numbers. 
pin_numbers = [3, 5, 7, 8, 10, 11, 13, 15, 16, 18, 19, 21, 22, 23, 24, 26]

## PWM frequncy
frequency = 50

## Bool to control when LEDs are active
LED_active = false

## Setup pwm data structure. Keys are pins. Values
##  are tuple of (duty cycle value, pwm reference)  
def pwm_setup():
    pins = {}
    for pin_num in pin_numbers:
        pins[pin_num] = [0]
        pins[pin_num] = [0, GPIO.PWM(pin_num, frequency)]
        pins[pin_num][1].start(0)
    return(pins)
    
## Cleanups pwm data structure.
def pwm_cleanup(pins):
    for pin_num in pin_numbers:
        pin_num[1].stop()
    GPIO.cleanup()

## Define pwm update loop which will run other thread
def pwm_loop():
    global pins
    while True
        for pin in pins:
            print(pin, pins[pin])
            # pin.ChangeDutyCycle(pins[pin])
        time.sleep(0.1)

## Updates pwm values for individual LEDs. Called when user hits submit.
def update_pwm(index, brightness):
    global pins
    pins[index] = brightness

## Start setup
pins = pwm_setup()

## Start pwm loop
try:
    thread.start_new_thread(pwm_loop, ())
except:
    print 'Couldn\'t create second thread'
    exit()
    
## Start web server via Flask
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def update_pwm():
    if request.method == 'POST':
        index = int(request.form.get('Index'))
        brightness = int(request.form.get('Brightness'))
        
        update_pwm(index, brightness)
        
        return( redirect ('/') )
    elif request.method == 'GET':
        return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
