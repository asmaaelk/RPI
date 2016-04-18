import time
import RPi.GPIO as GPIO

##GPIO.setmode(GPIO.BOARD)
##GPIO.setwarnings(False)
##
##GPIO.setup(11, GPIO.OUT)
##GPIO.setup(13, GPIO.OUT)
##GPIO.setup(15, GPIO.OUT)
##
##def turn_LED_on():
##    GPIO.output(11, GPIO.HIGH)
##    GPIO.output(13, GPIO.HIGH)
##    GPIO.output(15, GPIO.HIGH)
## 
##def turn_LED_off():
##    GPIO.output(11, GPIO.LOW)
##    GPIO.output(13, GPIO.LOW)
##    GPIO.output(15, GPIO.LOW)
##
##turn_LED_on()
##time.sleep(3)
##turn_LED_off()

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)

p1 = GPIO.PWM(11, 50) #channel = 11 frequency = 50Hz
p2 = GPIO.PWM(13, 50) #channel = 13 frequency = 50Hz
p3 = GPIO.PWM(15, 50) #channel = 15 frequency = 50Hz

p1.start(0)
p1.ChangeDutyCycle(10)
time.sleep(2)
p1.ChangeDutyCycle(50)
time.sleep(2)

#p2.start(0)
#p3.start(0)
##
##try:
##    while 1:
##        for dc in range(0, 100, 5):
##            p1.ChangeDutyCycle(dc)
##            p2.ChangeDutyCycle(dc)
##            p3.ChangeDutyCycle(dc)
##            time.sleep(0.1)
##        for dc in range(100, -1, -5):
##            p1.ChangeDutyCycle(dc)
##            p2.ChangeDutyCycle(dc)
##            p3.ChangeDutyCycle(dc)
##            time.sleep(0.1)
##except KeyboardInterrupt:
##    pass
p1.stop()
#p2.stop()
#p3.stop()
GPIO.cleanup()

##        if request.form['submit'] == 'Turn On':
##            turn_all_on()
##            return( redirect ('/') )
##        elif request.form['submit'] == 'Turn Off':
##            turn_all_off()
##            return( redirect ('/') )
##        elif request.form['submit'] == 'Toggle Red':
##            toggle_red()
##            return( redirect ('/') )
##        elif request.form['submit'] == 'Toggle Green':
##            toggle_green()
##            return( redirect ('/') )
##        elif request.form['submit'] == 'Toggle Yellow':
##            toggle_yellow()
##            return( redirect ('/') )


