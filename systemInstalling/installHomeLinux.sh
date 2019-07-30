#!/bin/bash

mydir=$(cat /etc/issue.net)

#update system
    
echo "\033[31mUpdate system\033[0m"
apt update
apt full-upgrade -y #работает

echo "\033[31mUpdate some packages\033[0m"
PACKAGES="build-essential libgtk2.0-dev pkg-config libavcodec-dev libavformat-dev libswscale-dev  libsm6 libxrender1 libfontconfig1
python-dev python-numpy libtbb2 libtbb-dev libjpeg-dev libpng-dev libtiff-dev libdc1394-22-dev apt-transport-https ca-certificates curl software-properties-common
gcc g++ gcc-multilib git python3-pip snapd qt5-default gnome-tweak-tool gparted python3-pyqt5 pyqt5-dev-tools gnuplot tmux gdb filezilla htop okular redis-server
mysql-server mysql-client sqlite3" 
apt-get -y --upgrade install $PACKAGES

snap install node --channel=latest/edge --classic

SNAP_PACKAGES="chromium telegram-desktop travis"
snap install $SNAP_PACKAGES
CLASSIC_PACKAGES="heroku code pycharm-professional"
snap install CLASSIC_PACKAGE --classic
TEST_SNAP_PACKAGES="arduino-mhall119 postman onlyoffice-desktopeditors snap-store"
snap install $TEST_SNAP_PACKAGES


curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu bionic stable"
apt-get update
apt-get install -y docker-ce

usermod -aG docker $USER
usermod -a -G dialout $USER #для портов ардуино

PYTHON_PACKAGES="wget cmake colorama sqlalchemy flask gitPython tqdm imutils imgaug python-dotenv docker rq redis
opencv-python==3.4.2.16 opencv-contrib-python==3.4.2.16
pandas https://github.com/OlafenwaMoses/ImageAI/releases/download/2.0.3/imageai-2.0.3-py3-none-any.whl mrcnn"

pip3 install setuptools
pip3 install $PYTHON_PACKAGES


bash ./cloneRepositories.sh
mysql_secure_installation


#удаление программ #справедливо для linux mint
PACKAGES_DELETE="rhythmbox hexchat thunderbird simple-scan"
echo "\033[31m DELETED\033[0"
apt-get -y remove $PACKAGES_DELETE

apt-get autoremove
#git
echo "\033[31mGit\033[0m"
git config --global user.email "sapfir999999@yandex.ru"
git config --global user.name "Sapfir0"

ssh-keygen -t rsa -b 4096 -C "sapfir999999@yandex.ru"


# для Mask R-CNN
git clone https://github.com/matterport/Mask_RCNN.git 
cd Mask_RCNN 
pip3 install -r requirements.txt 
python3 setup.py build  
python3 setup.py install 
cd ..  
rm -rf Mask_RCNN



