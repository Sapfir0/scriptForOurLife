port="/dev/ttyUSB0"
for i in "${dir}"/*; do
    if [ -d "$i" ]; then
        echo -e "${RED}${bold}Skipping directory:${NC}${normal} $i"
    elif [ -f "$i" ]; then
        if [[ "$i" == *py ]]; then
            echo -e "${GREEN}${bold}Putting:${NC}${normal} $i"
            eval "ampy --port ${port} put \"$i\""
            sleep 3s
        elif [[ "$i" != "${dir}/${me}" ]]; then
            echo -e "${RED}${bold}Skipping:${NC}${normal} $i"
        fi
    fi
done
ampy -p /dev/ttyUSB0 run main.py

