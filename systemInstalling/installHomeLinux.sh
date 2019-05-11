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

    #add-apt-repository -y ppa:slytomcat/ppa #yandex-indicator
    add-apt-repository -y ppa:ubuntu-desktop/ubuntu-make #среды разработок
    add-apt-repository -y ppa:danielrichter2007/grub-customizer #grub
    
    echo "\033[31mUpdate system\033[0m"
    apt update
    apt full-upgrade -y #работает
#qtchooser
    echo "\033[31mUpdate some packages\033[0m"
    PACKAGES="gcc g++ gcc-multilib virtualbox steam radiotray snapd git pulseaudio
    csh vim vim-runtime fasm meld qt5-default gnome-tweak-tool nautilus-dropbox yum npm 
    gnome-tweak-tool python3-pyqt5 pyqt5-dev-tools ubuntu-make gnuplot tmux gdb grub-customizer
    wine-stable wine32 filezilla htop okular" 
    apt-get -y install $PACKAGES

    umake ide atom
    
    PACKAGES1="spotify chromium discord telegram-desktop gitkraken"
    snap install $PACKAGES1
    snap install vscode --classic

#удаление программ #справедливо для linux mint
PACKAGES_DELETE="rhythmbox hexchatm thunderbird simple-scan"
    echo "\033[31m DELETED\033[0"
    apt -y remove $PACKAGES_DELETE

#encfs
  #  echo "\033[31mEncfs\033[0m"
  #   apt-get -y install encfs
  #  mkdir -p ~/encrypted 
  #  mkdir -p ~/decrypted 
  #  encfs ~/encrypted ~/decrypted #first inicialization
    sudo pip3 install PyQt5
#git
    echo "\033[31mGit\033[0m"
    git config --global user.email "sapfir999999@yandex.ru"
    git config --global user.name "Sapfir0"

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
        y|Y) wget http://ftp.fau.de/qtproject/archive/qt/5.11/5.11.1/qt-opensource-linux-x64-5.11.1.run;;
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