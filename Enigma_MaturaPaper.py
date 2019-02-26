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
    S1 = Scrambler(3, Scramblers[SL1], [SL1, SL2, SL3], SP1, RP[0]) ##Left scrambler in the machine
    S2 = Scrambler(2, Scramblers[SL2], [SL1, SL2, SL3], SP2, RP[1]) ##Middle Scrambler in the machine
    S3 = Scrambler(1, Scramblers[SL3], [SL1, SL2, SL3], SP3, RP[2]) ##Right Scrambler in the machine
    BP = {value: key for key, value in PB.items()} #Creating a Second Dictionary with the reversed keys
    ScramblerText.close() #Important to close the File -->  Otherwise it corupts
    S1.RingSetting, S2.RingSetting, S3.RingSetting ##Applies ring setting

    for x in range(100): ##Only for debugging
        l = "a"
        l = l.upper() ##First I change all the letters that are inputted to an uppercase letter for simplicity and originality
        pbo = Plugboard(l, PB, BP)
        so = S1.forward(S2.forward(S3.forward(pbo)))
        rf0 = Scramblers[5][so]
        rf = S3.backward(S2.backward(S1.backward(rf0)))
        ##Checking whether the letter is in the Plugboard or not
        if rf in PB:
            pbor = PB[rf]
            print(pbor, end="")
        elif rf in BP:
            pbor = BP[rf]
            print(pbor, end="")
        else:
            print(rf, end="")


class Scrambler(object):
    def __init__(self, Position, Wiring, Scramb, State, RingPosition):
        #Declaring the Variables for the class
        self.Position = Position
        self.Wiring = Wiring
        self.Scramb = Scramb
        self.TurnOverNotch = Scramblers[6]
        self.State = State
        self.RingPosition = RingPosition

    def RingSetting(self):
        """Changes the ring setting"""
        c = copy(self.Wiring)
        ring = self.RingPosition - 1
        if ring == 0 :
            return self.wiring
        else:
            for i in range(ring):
                for x in range(26):
                    self.Wiring[chr(i + 65)] = c[chr(((i + 1) % 26) + 65)]
            return self.Wiring

    def forward(self, letter):
        """Foreward movement through the """
        lnumber = ord(letter) - 65
        self.State = self.State % 26
        if self.Position == 1:
            self.State += 1
            letter_new = chr(((ord(self.Wiring[chr((lnumber + self.State)%26 + 65)]) - 65 - self.State )% 26) + 65)
        elif self.Position == 2:
            if self.State == ord(self.TurnOverNotch[self.Scramb[0]])-65:
                self.State += 1
                letter_new = chr(((ord(self.Wiring[chr((lnumber + self.State)%26 + 65)]) - 65 - self.State )% 26) + 65)
            else:
                letter_new = chr(((ord(self.Wiring[chr((lnumber + self.State)%26 + 65)]) - 65 - self.State )% 26) + 65)
        elif self.Position == 3:
            if self.State == ord(self.TurnOverNotch[self.Scramb[1]])-65:
                self.State += 1
                letter_new = chr(((ord(self.Wiring[chr((lnumber + self.State)%26 + 65)]) - 65 - self.State )% 26) + 65)
            else:
                letter_new = chr(((ord(self.Wiring[chr((lnumber + self.State)%26 + 65)]) - 65 - self.State )% 26) + 65)
        return letter_new

    def backward(self, letter):
        lnumber = ord(letter) - 65
        reverse = {value: key for key, value in self.Wiring.items()}
        if self.Position == 1:
            letter_new = chr(((ord(reverse[chr((lnumber + self.State)%26 + 65)]) - 65 - self.State) % 26) + 65)
        elif self.Position == 2:
            letter_new = chr(((ord(reverse[chr((lnumber + self.State)%26 + 65)]) - 65 - self.State) % 26) + 65)
        elif self.Position == 3:
            letter_new = chr(((ord(reverse[chr((lnumber + self.State)%26 + 65)]) - 65 - self.State) % 26) + 65)
        return letter_new

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
SP = ["A","B","C"]
PB = {
    "A":"G",
    "H":"Q",
    "O":"C",
    "Z":"Y",
    "N":"M",
    "T":"K"
}
RP = [1,1,1]
##Call Function Enigma
Enigma(SL, SP, PB, RP, "A")
