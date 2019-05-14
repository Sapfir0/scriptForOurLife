import configCluster as cfg

command = [ 
    "ls",
    "git clone https://github.com/avdosev/metida",
]

gitClone =  "git clone https://github.com/avdosev/metida"
clusterPath = cfg.username + cfg.hostname
portSettings = " -P " + cfg.port

npm = [
    "cd metida",
    "npm i",
    "npm start"
]



