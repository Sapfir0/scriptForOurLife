import requests
import os

link="https://api.github.com/sapfir0/keys"

keyFile = os.path.join(os.path.expanduser("~"), ".ssh", "id_rsa.pub")

with open(keyFile) as f:
    key = f.read()

data={"title": os.uname()[1], "key": key }
# проверить что такого названия нет

# аутентифицируемся

r = requests.post(link, data) #https://developer.github.com/v3/users/keys/
print(r.json())
