# RaspberryPi_ShutdownButton
This project describes how to make shutdown and reboot buttons for your raspberry pi


Contents of this project:
* shutdown.py: python code for reading GPIO buttons and shutting down/rebooting raspberry pi
* shutdown.service: service configuration file
* install.sh: install script for installing this service


Instructions:
* Unzip the release folder into the Documents folder of your Raspberry pi
* Change the reboot / shutdown pin numbers (here: 2 and 3) to the pins you want to use
    => NOTE: in GPIO pins are in BCM mode!
    => wire the buttons with one side to GND, the other to the respective pin numbers
* Also change the pull up/pull down configuration if necessary
* Run the install script by navigating to de ShutDown folder and run "sh install.sh"




Sources:
* http://www.diegoacuna.me/how-to-run-a-script-as-a-service-in-raspberry-pi-raspbian-jessie/    (how to install services)
* https://www.raspberrypi.org/forums/viewtopic.php?p=890295     (call system functions in python script)
* https://www.circuitbasics.com/how-to-write-and-run-a-shell-script-on-the-raspberry-pi/      (create bash scripts)
* https://sourceforge.net/p/raspberry-gpio-python/wiki/Inputs/      (GPIO tutorial)



