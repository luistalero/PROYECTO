import json
import os

MY_DATABASE = 'data/pacientes.json'

def NewFile(*param):
    with open(MY_DATABASE,"w") as wf:
        json.dump(param[0],wf,indent=4)

def UpdateFile(*param):
    with open(MY_DATABASE,'w') as wf:
        json.dump(param[0],wf,indent=4)

def AddData(*param):
    pacientes = list(param)
    with open(MY_DATABASE,"r+") as rwf:
        data_file=json.load(rwf)
        if (len(param) >1):
            data_file.update({pacientes[1]:pacientes[2]})
        else:
            data_file.update({param[0]})
        rwf.seek(0)
        json.dump(data_file,rwf,indent=4)

def ReadFile():
    with open(MY_DATABASE,"r") as rf:
        return json.load(rf)

def checkFile(*param):
    pacientes = list(param)
    if(os.path.isfile(MY_DATABASE)):
        if(len(param)):
            pass
    else:
        if(len(param)):
            NewFile(pacientes[0])