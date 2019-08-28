import os
from browsers.Mozilla import Mozilla
from browsers.Chromium import ChromiumSnap

import argparse


def configs():
    if not os.path.exists("config.py"):
        basicConfig = ["urls = [\"badUrl1\", \"badUrl2\", \"badUrln\"] \n",
                       "titles = [\"badTitle1\", \"badTitle2\", \"badTitlen\"]"]
        basicHelper = "\n# Specify the keywords for which the history will be deleted "
        print("Configs file was not found")
        with open('config.py', 'w') as f:
            for i in basicConfig:
                f.write(i)
            f.write(basicHelper)
            f.close()
            print("Open config.py for further instructions")
        return False
    return True


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('-m', '--mozilla', action="store_true")
    parser.add_argument('-c', '--chromium-snap', action="store_true")
    args = parser.parse_args()

    configs()
    if args.mozilla:
        Mozilla()
    elif args.chromium_snap:
        ChromiumSnap()

