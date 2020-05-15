Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))

set packages="vlc wget docker-desktop cmake steam postman cpu-z.install utorrent gpu-z.install filezilla ccleaner putty.install git.install adobereader 7zip.install"
set ide="pycharm webstorm jetbrains-rider vscode visualstudio2019community"
set browser="chromium firefox"
set language="nodejs.install mysql sqlite python3 jre8"
set services="netfx-4.7.1-devpack vcredist140 dotnetcore-sdk"

choco install -y %packages%
choco install -y %ide%
choco install -y %browser%
choco install -y %language%
choco install -y %services%

choco install -y utorrent --ignore-checksums