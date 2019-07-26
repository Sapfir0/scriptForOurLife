
wget -q http://micropython.org/resources/firmware/esp8266-20190726-v1.11-180-g8f55a8fab.bin
esptool.py --port /dev/ttyUSB0 erase_flash
esptool.py --port /dev/ttyUSB0 --baud 460800 write_flash --flash_size=detect 0 esp8266-20190726-v1.11-180-g8f55a8fab.bin

