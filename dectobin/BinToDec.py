def ToDEC(a):
    varList = list(a)
    for i in varList:
        if i != '1' and i != '0':
            return('error')
    try:
        while varList[0] == '0':
            varList.remove(varList[0])
        varList.remove(varList[0])
        decInProgress = 1
        for i in varList:
            if i == '0':
                decInProgress = decInProgress*2
            elif i == '1':
                decInProgress = decInProgress*2+1
        return(decInProgress)
    except:
        return('error')