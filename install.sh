#!/bin/bash
set -e

echo "Copy service config file to /lib/systemd/system folder..."
sudo cp shutdown.service /lib/systemd/system/shutdown.service

echo "Give permissions to file..."
sudo chmod 644 /lib/systemd/system/shutdown.service
sudo chmod +x /home/pi/Documents/ShutdownService/shutdown.py
echo "reload daemon"

sudo systemctl daemon-reload

echo "enable service"
sudo systemctl enable shutdown.service

echo "start service"
sudo systemctl start shutdown.service


echo "service installing completed"