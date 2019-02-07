import RPi.GPIO as GPIO
from subprocess import call

looping = True

GPIO.setmode(GPIO.BCM)

# configure shutdown and reboot pins here
shu = 3
reb = 2


GPIO.setup(shu,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(reb,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)

def shutdown(channel):
	setLoopingToFalse()
	print("shutdown!")
	call("sudo shutdown -h now", shell=True)

def reboot(channel):
	setLoopingToFalse()
	print("reboot!")
	call("sudo reboot", shell=True)

def setLoopingToFalse():
	global looping
	looping = False

GPIO.add_event_detect(shu,GPIO.FALLING,bouncetime=500)
GPIO.add_event_callback(shu,shutdown)

GPIO.add_event_detect(reb,GPIO.FALLING,bouncetime=500)
GPIO.add_event_callback(reb,reboot)


try:
	while looping:
		# Only purpose is to keep service running
        p=1
finally:
	GPIO.cleanup()