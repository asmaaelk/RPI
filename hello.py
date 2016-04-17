from flask import Flask, render_template, request, redirect
import RPi.GPIO as GPIO
import time

red_active, green_active, yellow_active, all_active = False, False, False, False

app = Flask(__name__)

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)

def turn_all_on():
    global red_active, green_active, yellow_active
    GPIO.output(11, GPIO.HIGH)
    GPIO.output(13, GPIO.HIGH)
    GPIO.output(15, GPIO.HIGH)
    red_active, green_active, yellow_active = True, True, True
 
def turn_all_off():
    global red_active, green_active, yellow_active
    GPIO.output(11, GPIO.LOW)
    GPIO.output(13, GPIO.LOW)
    GPIO.output(15, GPIO.LOW)
    red_active, green_active, yellow_active = False, False, False

def toggle_red():
    global red_active
    if red_active:
        GPIO.output(11, GPIO.LOW)
    else:
        GPIO.output(11, GPIO.HIGH)
    red_active = not red_active

def toggle_green():
    global green_active
    if green_active:
        GPIO.output(13, GPIO.LOW)
    else:
        GPIO.output(13, GPIO.HIGH)
    green_active = not green_active

def toggle_yellow():
    global yellow_active
    if yellow_active:
        GPIO.output(15, GPIO.LOW)
    else:
        GPIO.output(15, GPIO.HIGH)
    yellow_active = not yellow_active

def pinSetUP(index, brightness):
    p = GPIO.PWM(index, 50)
    p.start(0)
    p.ChangeDutyCycle(brightness)
    time.sleep(2)

@app.route('/', methods=['GET', 'POST'])
def hello_world():
    print str(request)
    #select = request.form.get('Index')
    if request.method == 'POST':
        turn_all_off()
        #print str(select)
        selected_index = request.form.get('Index')
        selected_brightness = request.form.get("Brightness")
        
        print str(selected_index)
        print str(selected_brightness)

        if selected_index:
            pinSetUP(int(selected_index), int(selected_brightness))
            
            
            
#        if selected_index == "15":
#            toggle_yellow()
#            return redirect('/')
        else:
            return( redirect ('/') )
    elif request.method == 'GET':
        return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)



