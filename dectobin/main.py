import BinToDec
import DecToBin

print('dectobin or bintodec')
hub = input('>')
while True:
    if hub == 'dectobin':
        print("""
            ██████  ███████  ██████ ████████  ██████  ██████  ██ ███    ██ 
            ██   ██ ██      ██         ██    ██    ██ ██   ██ ██ ████   ██ 
            ██   ██ █████   ██         ██    ██    ██ ██████  ██ ██ ██  ██ 
            ██   ██ ██      ██         ██    ██    ██ ██   ██ ██ ██  ██ ██ 
            ██████  ███████  ██████    ██     ██████  ██████  ██ ██   ████                                 
            """)
        while True:
            print("write an dec number")
            while True:
                try:
                    numDEC = int(input('>'))
                    break
                except:
                    print("error, not a number")
            print("Number you wrote is:", numDEC)
            print("This number in BIN is:", DecToBin.ToBIN(numDEC))
    elif hub == 'bintodec':
        print("""
                ██████  ██ ███    ██ ████████  ██████  ██████  ███████  ██████ 
                ██   ██ ██ ████   ██    ██    ██    ██ ██   ██ ██      ██      
                ██████  ██ ██ ██  ██    ██    ██    ██ ██   ██ █████   ██      
                ██   ██ ██ ██  ██ ██    ██    ██    ██ ██   ██ ██      ██      
                ██████  ██ ██   ████    ██     ██████  ██████  ███████  ██████
              """)
        while True:
            print('write an bin number')
            while True:
                numBIN = input('>')
                if BinToDec.ToDEC(numBIN) != 'error':
                    break
                else:
                    print('error, not a binary number')
            print('Number you wrote is:', numBIN)
            print('this number in DEC is:', BinToDec.ToDEC(numBIN))
