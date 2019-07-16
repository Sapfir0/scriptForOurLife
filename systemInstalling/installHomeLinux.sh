#!/bin/bash

mydir=$(cat /etc/issue.net)

OPTION=$(whiptail --title "$mydir" --menu "Choise your packet" 15 60 4 \
    "1" "Setup default packet" \
    "2" "Setup advanced packet(without sudo)" \
    "3" "Custom setup" \
    "4" "About me" 3>&1 1>&2 2>&3)
exitstatus=$?
if [ $exitstatus = 0 ]; then
    echo "Вы выбрали стандартную установку:" $OPTION
else
    echo "Вы нажали отмену."
fi



if [ $OPTION = 1 ]; then #стандартная установка
#update system
    
    echo "\033[31mUpdate system\033[0m"
    apt update
    apt full-upgrade -y #работает

    echo "\033[31mUpdate some packages\033[0m"
    PACKAGES="gcc g++  apt-transport-https ca-certificates curl software-properties-common 
    gcc-multilib libsm6 libxrender1 git
    libfontconfig1 python3-pip snapd qt5-default gnome-tweak-tool gparted python3-pyqt5 
    pyqt5-dev-tools gnuplot tmux gdb wine-stable wine32 filezilla htop okular 
    mysql-server mysql-client sqlite3 nodejs" 
    apt-get -y --upgrade install $PACKAGES

    curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
    add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu bionic stable"
    apt-get update
    apt-get install -y docker-ce

    curl -sL https://deb.nodesource.com/setup_6.x -o nodesource_setup.sh
    bash nodesource_setup.sh
    apt-get install -y nodejs


    PACKAGES1="chromium telegram-desktop travis"
    snap install $PACKAGES1
    snap install heroku --classic
    snap install code  --classic


    usermod -aG docker $USER
    usermod -a -G dialout $USER #для портов ардуино

    PYTHON_PACKAGES="wget cmake colorama sqlalchemy pandas https://github.com/OlafenwaMoses/ImageAI/releases/download/2.0.3/imageai-2.0.3-py3-none-any.whl mrcnn"
    pip3 install setuptools
    pip3 install $PYTHON_PACKAGES

    # для Mask R-CNN
    git clone https://github.com/matterport/Mask_RCNN.git 
    cd Mask_RCNN 
    pip3 install -r requirements.txt 
    python3 setup.py build  
    python3 setup.py install 
    cd ..  
    rm -rf Mask_RCNN


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

#############################################################
elif  [ $OPTION = 2 ]; then #advanced

    cd
    mkdir installed
    cd ~/installed
    
    git clone https://github.com/Dman95/SASM
    cd ~/installed/SASM
    qmake
    make
    make install sasm
    
    cd /tmp
    git clone git://github.com/GM-Script-Writer-62850/Ubuntu-Mainline-Kernel-Updater
    bash Ubuntu-Mainline-Kernel-Updater/install
    
#QT установка с GUI
    echo "\033[31mQT\033[0m"
    echo "\033[31mDo you want to download offline packages?\033[0m (y/n)"

    read item
    case "$item" in
        y|Y) wget http://ftp.fau.de/qtproject/archive/qt/5.12/5.12.3/qt-opensource-linux-x64-5.12.3.run;;
        #cd ~/Загрузки/;

        n|N) wget http://download.qt.io/official_releases/online_installers/qt-unified-linux-x64-online.run;;
        #cd ~/Downloads/ ;;
        #chmod u+x qt-opensource-linux-x64-5.11.1.run
        #./qt-opensource-linux-x64-5.11.1.run;
    esac

####################################################
elif [ $OPTION = 3 ]; then 


OPTION=$(whiptail --title "Установка доп. пакетов" --menu "Что ты хочешь" 15 60 4 \
    "1" "Android studio" \
    "2" "Gradle&JDK" \
    "3" "Chromium" \
    "4" "---" 3>&1 1>&2 2>&3)
exitstatus=$?
if [ $exitstatus = 0 ]; then
    echo "Вы выбрали установку:" $OPTION
else
    echo "Вы нажали отмену."
fi
    if [ $OPTION=1 ]; then
#android-studio
    echo "\033[31mAndroid-studio\033[0m"
    snap install android-studio --classic

    elif [ $OPTION=2 ]; then
#gradle
echo "\033[31mGradle\033[0m"
    add-apt-repository ppa:cwchien/gradle
    apt-get update
    apt-get install gradle
    elif [ $OPTION=3 ]; then
    fi

fi