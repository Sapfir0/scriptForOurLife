NAME=$(uname -n)
curl -u "$1:$2" --data '{"title":"'"$NAME"'","key":"'"$(cat ~/.ssh/id_rsa.pub)"'"}' https://api.github.com/user/keys



