import os
import paramiko
import configCluster as cfg
import commandList as cl


class VSTU_CLuster:
    def __init__(self):
        self.client = paramiko.SSHClient()
        self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())# данная строчка решает проблему с known_hosts

    def connect(self):
        self.client.connect(hostname=cfg.hostname, username=cfg.username, password=cfg.password, port=cfg.port)

    def runCommand(self, command):
        stdin, stdout, stderr = self.client.exec_command(command)
        if ( stderr.read() != None):
            print(stderr.read())
        print(stdout.read())

    def downloadMetida(self):
        self.runCommand(cl.gitClone)

    def pushToServer(self, inputDir, outputDir):
         #scp -P $port $1 $loginOnCluster$clustersUrl:$2
        self.runCommand("scp" + cl.portSettings + " "  + inputDir + " " + cl.clusterPath + ":" + outputDir) 
    
    def getFromServer(self, inputDir, outputDir):
        # scp -P $port $loginOnCluster$clustersUrl:$1 $2
        self.runCommand("scp" + cl.portSettings + " " + cl.clusterPath + ":" + inputDir + " " + outputDir) 

    def connectToNode(self, nodeNumber):
        self.runCommand("ssh node" + nodeNumber)  #без пробела

    # def workWithNpm(self):
    #     self.runCommand()

    def disconnect(self):
        self.client.close()




