Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))


choco install -y vlc docker-desktop steam postman git adobereader 7zip
choco install -y vscode visualstudio2019community
choco install -y chromium firefox discord telergram
choco install -y nodejs mysql sqlite python3 jre8 yarn heidisql
choco install -y jetbrainstoolbox  

choco install -y utorrent --ignore-checksums