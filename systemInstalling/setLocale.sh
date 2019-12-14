#!/bin/bash

apt-get install language-pack-ru
dpkg-reconfigure locales
dpkg-reconfigure keyboard-configuration
dpkg-reconfigure console-setup
