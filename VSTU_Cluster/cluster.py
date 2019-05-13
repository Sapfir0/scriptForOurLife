import os
import paramiko
import configCluster as cfg


client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())# данная строчка решает проблему с known_hosts
client.connect(hostname=cfg.hostname, username=cfg.username, password=cfg.password, port=cfg.port)

stdin, stdout, stderr = client.exec_command('git clone https://github.com/avdosev/metida && cd metida && npm i && npm start ')
data = stdout.read() + stderr.read()
print(data)
client.close()


# print(data)

