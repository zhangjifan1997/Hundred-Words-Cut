def NotYet():
    fNotYet=open("NotYet","r+")
    notYet=fNotYet.readlines()
    for number in range(0,len(notYet)):
        notYet[number]=int(notYet[number])
    return notYet
def Cutted():
    fCutted=open("Cutted","r+")
    cutted=fCutted.readlines()
    for number in range(0,len(cutted)):
        cutted[number]=int(cutted[number])
    return cutted
def WordList():
    fNotYet=open("WordList","r+")
    wordList=fNotYet.readlines()
    for i in range(0,len(wordList)):
        wordList[i]=wordList[i][0:-1]
    return wordList
