#!/bin/bash
sudo apt-get update && sudo apt-get upgrade -y
sudo apt-get -y install xorg gdm3 xrdp xserver-xorg xauth libx11-dev
sudo apt-get -y install libminizip1 libxcb-glx0
sudo apt-get update && sudo apt-get upgrade -y
sudo dpkg -i teamviewer-host_15.35.7_arm64.deb
