#!/bin/bash
set -e

echo "Stopping service..."
sudo systmctl stop shutdown.service

echo "Start deleting service ..."
sudo rm /lib/systemd/system/shutdown.service