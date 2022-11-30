#! /bin/bash
# 윗 줄은 이 프로그램은 bash를 기반으로 실행된다는 뜻입니다.
sudo apt-get update && sudo apt-get upgrade -y;

# tomcat 설치합니다.(제외)
# echo "Installing tomcat9-admin ..."
# sudo apt-get install -y tomcat9 tomcat9-admin

# mariadb 설치합니다.
echo "Installing mariadb-server ..."
sudo apt install -y mariadb-server;

# c++ mariadb install
echo "Installing c++ mariadb library ..."
sudo apt install  -y libmariadb3 libmariadb-dev;

# IoT python sensor용 start ====================================
# pip install
echo "Installing pip ..."
sudo apt-get install -y python3-pip;

# python process set-title library install
echo "Installing setproctitle library ..."
sudo pip3 install --ignore-installed setproctitle;

# sensor pyserial library install
echo "Installing pyserial library ..."
sudo pip3 install --ignore-installed pyserial;

# numpy library install
echo "Installing numpy library ..."
sudo pip3 install --ignore-installed numpy;

# GPS 용 pynmea2 library install
echo "Installing pynmea2 library ..."
sudo pip3 install --ignore-installed pynmea2;

# GPS Monitoring library install
echo "gps monitoring install..."
sudo apt install -y gpsd-clients gpsd;

# opencv-python library install
echo "Installing opencv-python library ..."
sudo pip3 install --ignore-installed opencv-python;

# pymysql library install
echo "Installing pymysql library ..."
sudo pip3 install --ignore-installed pymysql;

# websockets library install
echo "Installing websockets library ..."
sudo pip3 install --ignore-installed websockets;
# IoT python sensor용 end ====================================

# libopenal-dev library install
echo "Installing libopenal-dev library ..."
sudo apt-get install -y libopenal-dev;

# libsndfile-dev library install
echo "Installing libsndfile-dev library ..."
sudo apt-get install -y libsndfile-dev;

# cmake library install
echo "Installing cmake library ..."
sudo apt-get install -y cmake;

#startup install
echo "Installing starup ..."  
sudo apt install  -y gnome-startup-applications;

#java install
echo "Installing java ..."
sudo apt-get install -y openjdk-11-jdk;

#update & upgrade
sudo apt-get update && sudo apt-get upgrade -y

# chromium-browser 설치합니다.
echo "Installing chromium-browser ..."
sudo apt-get install -y chromium-browser;

#setup End
echo "setup Done!"