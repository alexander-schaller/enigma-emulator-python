import json
from copy import *
##ScramblerWiring info is opened --> and json information extracted
ScramblerText = open('ScramblerText.txt', 'r')
Scramblers = json.load(ScramblerText)

##Main Function
def Enigma (SL, SP, PB, RP, word):
    """SL (Scrambler Location, List of 3 Scramblers)
    SP (Scrambler Position, List of 3 Letters you can see on the machine)
    PB (Plugboard, Dictionary with 0 - 13 Letters connecting with eachother)
    RP (Ring Position, List of 3 Numbers from 1 - 26)
    l (Input letter)"""
    SL1, SL2, SL3 = ScramblerNum[SL[0]], ScramblerNum[SL[1]], ScramblerNum[SL[2]] ## Turns the Three roman numerals of the scrambler into Numbers
    SP1, SP2, SP3 = ord(SP[0]) - 65, ord(SP[1]) - 65, ord(SP[2]) - 65 ##Turn State into Numbers
    ## Creates the 3 Scramblers with the specific information
    S1 = Scrambler(Scramblers[SL1], Scramblers[6][SL1], SP1, RP[0]) ##Left scrambler in the machine
    S2 = Scrambler(Scramblers[SL2], Scramblers[6][SL2], SP2, RP[1]) ##Middle Scrambler in the machine
    S3 = Scrambler(Scramblers[SL3], Scramblers[6][SL3], SP3, RP[2]) ##Right Scrambler in the machine
    BP = {value: key for key, value in PB.items()} #Creating a Second Dictionary with the reversed keys
    ScramblerText.close() #Important to close the File -->  Otherwise it corupts
    S1.RingSetting(), S2.RingSetting(), S3.RingSetting() ##Applies ring setting

    for l in word: ##Only for debugging
        l = l.upper() ##First I change all the letters that are inputted to an uppercase letter
        pbo = Plugboard(l, PB, BP)

        ##Forward through Scramblers
        x, y = 0,0
        lnumber = ord(pbo) - 65
        S3.forward()
        x += 1
        letter_new1 = chr(((ord(S3.Wiring[chr((lnumber + S3.State - S3.RingPosition)%26 + 65)]) - 65 - S3.State + S3.RingPosition)% 26) + 65)
##        print(letter_new1, end=" / ")
        if S3.State == ord(S3.TurnOverNotch) - 65 and x % 26 == 1:
            S2.forward()
            letter_new2 = chr(((ord(S2.Wiring[chr((ord(letter_new1) - 65 + S2.State - S2.RingPosition)%26 + 65)]) - 65 - S2.State + S2.RingPosition)% 26) + 65)
##            print(letter_new2, end=" / ")
        else:
            letter_new2 = chr(((ord(S2.Wiring[chr((ord(letter_new1) - 65 + S2.State - S2.RingPosition)%26 + 65)]) - 65 - S2.State + S2.RingPosition)% 26) + 65)
##            print(letter_new2, end=" / ")
        if S2.State == ord(S2.TurnOverNotch) - 65: #and y % 26 == 1:
            S1.forward()
            letter_new3 = chr(((ord(S1.Wiring[chr((ord(letter_new2) - 65 + S1.State - S1.RingPosition)%26 + 65)]) - 65 - S1.State + S1.RingPosition)% 26) + 65)
##            print(letter_new3, end=" / ")
        else:
            letter_new3 = chr(((ord(S1.Wiring[chr((ord(letter_new2) - 65 + S1.State - S1.RingPosition)%26 + 65)]) - 65 - S1.State + S1.RingPosition)% 26) + 65)
##            print(letter_new3, end=" / ")
        print(chr(S1.State + 65), chr(S2.State + 65), chr(S3.State + 65), end=" / ")

        ##Back through Scramblers
        rf0 = Scramblers[5][letter_new3]
##        print(rf0, end=" / ")
        reverse1 = {value: key for key, value in S1.Wiring.items()}
        reverse2 = {value: key for key, value in S2.Wiring.items()}
        reverse3 = {value: key for key, value in S3.Wiring.items()}
        letter_back1 = chr(((ord(reverse1[chr((ord(rf0) - 65 + S1.State - S1.RingPosition)%26 + 65)]) - 65 - S1.State + S1.RingPosition) % 26) + 65)
##        print(letter_back1, end=" / ")
        letter_back2 = chr(((ord(reverse2[chr((ord(letter_back1) - 65 + S2.State - S2.RingPosition)%26 + 65)]) - 65 - S2.State + S2.RingPosition) % 26) + 65)
##        print(letter_back2, end=" / ")
        rf = chr(((ord(reverse3[chr((ord(letter_back2) - 65 + S3.State - S3.RingPosition)%26 + 65)]) - 65 - S3.State + S3.RingPosition) % 26) + 65)
##        print(rf)

        ##Checking whether the letter is in the Plugboard or not
##        if rf in PB:
##            pbor = PB[rf]
####            print(pbor, end = "")
##        elif rf in BP:
##            pbor = BP[rf]
####            print(pbor, end = "")
##        else:
####            print(rf, end = "")


class Scrambler(object):
    def __init__(self, Wiring, TurnOverNotch, State, RingPosition):
        #Declaring the Variables for the class
        self.Wiring = Wiring
        self.TurnOverNotch = TurnOverNotch
        self.State = State
        self.RingPosition = RingPosition

    def RingSetting(self):
        """Changes the ring setting"""
        self.RingPosition -= 1

    def forward(self):
        self.State += 1
        self.State %= 26

    def backward(self):
        self.State -= 1
        self.State %= 26

def Plugboard(l, PB, BP):
    ##If the letter is in the Plugboard(PB) then it changes its value otherwise it keeps it.
    if l in PB:
        pbo = PB[l]
    elif l in BP:
        pbo = BP[l]
    else:
        pbo = l
    return pbo



##Changes roman numerals to Python Indices
ScramblerNum = {"I":0,"II":1,"III":2,"IV":3,"V":4}

##Input Values
SL = ["I","II","III"]
SP = ["A","D","T"]
PB = {}
RP = [1,1,1]
##Call Function Enigma
Enigma(SL, SP, PB, RP, "Alex")
