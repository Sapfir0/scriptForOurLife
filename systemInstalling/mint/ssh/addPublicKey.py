import subprocess

print("Print your login on github:")
login = input()
print("Print your password ( ͡° ͜ʖ ͡°) ure creditionals are protected")
password = input()


args = ["bash", "./addSshKeyToGithub.sh", login, password]
process = subprocess.Popen(args, stdout=subprocess.PIPE)
data = process.communicate()
print(data)

