Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))


choco install -y vlc docker-desktop steam postman ccleaner git adobereader 7zip
choco install -y pycharm webstorm vscode visualstudio2019community
choco install -y chromium firefox
choco install -y nodejs.install mysql sqlite python3 jre8

choco install -y utorrent --ignore-checksums