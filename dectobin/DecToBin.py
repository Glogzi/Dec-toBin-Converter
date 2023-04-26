def ToBIN(a):
    #list for binary numbers
    OnesAndZeros = []
    while a != 1:
        if a%2 != 0:
            OnesAndZeros.insert(0, 1)
            a -= 1
            a = a/2
        else:
            OnesAndZeros.insert(0, 0)
            a = a/2
    OnesAndZeros.insert(0, 1)
    #changes list elements to one string, that's what map does
    Output = ''.join(map(str, OnesAndZeros))
    return(Output)