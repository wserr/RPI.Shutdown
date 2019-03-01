import os
import time
import RPi.GPIO as GPIO
import logging

looping = True

GPIO.setmode(GPIO.BCM)

# logging
logging.basicConfig(level = logging.INFO, filename = time.strftime("%Y-%m-%d.log"), format = '%(asctime)s  %(levelname)-10s %(processName)s  %(name)s %(message)s')

# configure shutdown and reboot pins here
shu = 3
reb = 2


GPIO.setup(shu,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(reb,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)

def shutdown(channel):
	setLoopingToFalse()
	logging.info("System shutdown requested")
	os.system("sudo shutdown -h now")

def reboot(channel):
	setLoopingToFalse()
	logging.info("System reboot requested")
	os.system("sudo shutdown -r now")

def setLoopingToFalse():
	GPIO.cleanup()
	global looping
	looping = False

GPIO.add_event_detect(shu,GPIO.FALLING,callback = shutdown, bouncetime=500)

GPIO.add_event_detect(reb,GPIO.FALLING,callback = reboot, bouncetime=500)


while looping:
	# Only purpose is to keep service running
        time.sleep(1)
