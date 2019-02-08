#!/bin/bash
set -e

echo "Stopping service..."
sudo systemctl stop shutdown.service

echo "Start deleting service ..."
sudo rm /lib/systemd/system/shutdown.service

echo "Deleting completed."
