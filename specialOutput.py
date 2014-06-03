def NewNotYet(notYet):
    fNotYet=open("NotYet","w")
    for number in range(0,len(notYet)):
        notYet[number]=str(notYet[number])+'\n'
    fNotYet.seek(0)
    fNotYet.truncate()
    fNotYet.writelines(notYet)
def NewCutted(cutted):
    fCutted=open("Cutted","w")
    for number in range(0,len(cutted)):
        cutted[number]=str(cutted[number])+'\n'
    fCutted.seek(0)
    fCutted.truncate()
    fCutted.writelines(cutted)
def Redo():
    fNotYet=open("NotYet","w")
    fCutted=open("Cutted","w")
    fCutted.truncate()
    fNotYet1=open("NotYet1","r+")
    notYet=fNotYet1.readlines()
    fNotYet.writelines(notYet)
