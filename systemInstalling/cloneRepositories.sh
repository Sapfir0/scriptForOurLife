cd ~
git clone git@github.com:avdosev/metida.git
git clone git@github.com:Sapfir0/Meteo-Server.git
git clone git@github.com:Sapfir0/premier-eye.git
git clone git@github.com:Sapfir0/meteostation.git
git clone git@github.com:Sapfir0/scriptForOurLife.git

wget https://www.dropbox.com/s/ryz6q6cr6zygnle/settings.zip


# if files are locked root privilegies
chown sapfir -R Meteo-Server/
chown sapfir -R meteostation/
chown sapfir -R metida/
chown sapfir -R premier-eye/
chown sapfir -R scriptForOurLife/


