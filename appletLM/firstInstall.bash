ourDir=$(pwd)
cd
dir=".local/share/cinnamon/applets/cpu_checker@cinnamon.org"
mkdir -p $dir
cd 
cp "$ourDir/applet.js" "$dir/applet.js"
cp "$ourDir/metadata.json" "$dir/metadata.json"


