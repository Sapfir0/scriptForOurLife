
wget -q http://micropython.org/resources/firmware/esp8266-20190529-v1.11.bin
esptool.py --port /dev/ttyUSB0 erase_flash
esptool.py --port /dev/ttyUSB0 --baud 460800 write_flash --flash_size=detect 0 esp8266-20190529-v1.11.bin

