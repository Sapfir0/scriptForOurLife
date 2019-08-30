#!/bin/bash

RED='\033[0;31m'
GREEN='\033[0;32m'
NC='\033[0m' # No Color
bold=$(tput bold)
normal=$(tput sgr0)
mydistr=$(cat /etc/issue.net)
current_dir=$(pwd)

#update system
echo -e "${GREEN}${bold}Update system ${normal}${NC}";
apt-get update
apt-get dist-update

echo -e "${GREEN}${bold}Update some packages ${normal}${NC}";
PACKAGES="build-essential libgtk2.0-dev pkg-config libavcodec-dev libavformat-dev libswscale-dev  libsm6 libxrender1 libfontconfig1
python-dev libtbb2 libtbb-dev libjpeg-dev libpng-dev libtiff-dev libdc1394-22-dev apt-transport-https ca-certificates curl software-properties-common
gcc g++ gcc-multilib git python3-pip snapd gparted gnuplot tmux gdb filezilla htop okular redis-server 
mysql-server mysql-client sqlite3 telnet" 
apt-get -y --upgrade install $PACKAGES

echo -e "${GREEN}${bold}Snap ${normal}${NC}";
snap install node --channel=latest/edge --classic
SNAP_PACKAGES="chromium telegram-desktop travis jupyter"
snap install $SNAP_PACKAGES
snap install heroku --classic
snap install code --classic
snap install pycharm-professional --classic
snap install clion --classic
TEST_SNAP_PACKAGES="postman onlyoffice-desktopeditors"
snap install $TEST_SNAP_PACKAGES


curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu bionic stable"
apt-get update
apt-get install -y docker-ce docker-compose

usermod -aG docker $USER
usermod -aG dialout $USER #для портов ардуино

echo -e "${GREEN}${bold}Python pip packages ${normal}${NC}";
PYTHON_PACKAGES="wget cmake colorama sqlalchemy flask gitPython tqdm imutils imgaug python-dotenv docker rq redis
opencv-python==3.4.2.16 opencv-contrib-python==3.4.2.16
pandas https://github.com/OlafenwaMoses/ImageAI/releases/download/2.0.3/imageai-2.0.3-py3-none-any.whl mrcnn"
pip3 install setuptools
pip3 install $PYTHON_PACKAGES

#справедливо для linux mint
echo -e "${GREEN}${bold}Deleting packages ${normal}${NC}";
PACKAGES_DELETE="rhythmbox hexchat thunderbird simple-scan"
echo "\033[31m DELETED\033[0"
apt-get -y remove $PACKAGES_DELETE
apt-get remove -y libreoffice*

apt-get autoremove

EMAIL="sapfir999999@yandex.ru"
LOGIN="Sapfir0"
echo -e "${GREEN}${bold}Git config ${normal}${NC}";
git config --global user.email $EMAIL
git config --global user.name $LOGIN
ssh-keygen -t rsa -b 4096 -C $EMAIL
python3 "ssh/addPublicKey.py"

echo -e "${GREEN}${bold}Downloading git repos ${normal}${NC}";
bash ./cloneRepositories.sh

echo -e "${GREEN}${bold}MySQL config ${normal}${NC}";
mysql_secure_installation



