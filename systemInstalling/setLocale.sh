#!/bin/bash

#настройка локалей, если не настроена
apt-get install language-pack-ru
dpkg-reconfigure locales
dpkg-reconfigure keyboard-configuration
dpkg-reconfigure console-setup
