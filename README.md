# RaspberryPi_ShutdownButton
This project describes how to make shutdown and reboot buttons for your raspberry pi


Contents of this project:
* shutdown.py: python code for reading GPIO buttons and shutting down/rebooting your raspberry pi

Instructions:
* Get the repository by cloning from git: https://github.com/willemserruys/RaspberryPi_ShutdownButton/
* Change the reboot / shutdown pin numbers (here: 2 and 3) to the pins you want to use
    * NOTE: in GPIO pins are in BCM mode!
    * wire the buttons with one side to GND, the other to the respective pin numbers you chose
* Add the python script to /etc/rc.local
* reboot your raspberry pi

Sources:
* https://www.hackster.io/glowascii/raspberry-pi-shutdown-restart-button-d5fd07 (how to make a restart button for RPi)



OUTDATED
I tried creating a service at first, but this didn't work very well.
The shutdown was delayed for about a minute or 2.
* http://www.diegoacuna.me/how-to-run-a-script-as-a-service-in-raspberry-pi-raspbian-jessie/    (how to install services)
* https://www.raspberrypi.org/forums/viewtopic.php?p=890295     (call system functions in python script)
* https://www.circuitbasics.com/how-to-write-and-run-a-shell-script-on-the-raspberry-pi/      (create bash scripts)
* https://sourceforge.net/p/raspberry-gpio-python/wiki/Inputs/      (GPIO tutorial)





