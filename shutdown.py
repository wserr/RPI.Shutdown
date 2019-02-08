import os
import time
import RPi.GPIO as GPIO

looping = True

GPIO.setmode(GPIO.BCM)

# configure shutdown and reboot pins here
shu = 3
reb = 2


GPIO.setup(shu,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(reb,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)

def shutdown(channel):
	setLoopingToFalse()
	os.system("sudo shutdown -h now")

def reboot(channel):
	setLoopingToFalse()
	os.system("sudo shutdown -r now")

def setLoopingToFalse():
	global looping
	looping = False

GPIO.add_event_detect(shu,GPIO.FALLING,bouncetime=500)
GPIO.add_event_callback(shu,shutdown)

GPIO.add_event_detect(reb,GPIO.FALLING,bouncetime=500)
GPIO.add_event_callback(reb,reboot)


while looping:
	# Only purpose is to keep service running
        time.sleep(1)
