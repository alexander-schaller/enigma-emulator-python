import json
from copy import *

##ScramblerWiring info is opened --> and json information extracted
ScramblerText = open('ScramblerText.txt', 'r')
Scramblers = json.load(ScramblerText)


##Main Function
def Enigma(SL, SP, PB, RP, l):
    """SL (Scrambler Location, List of 3 Scramblers)
    SP (Scrambler Position, List of 3 Letters you can see on the machine)
    PB (Plugboard, Dictionary with 0 - 13 Letters connecting with eachother)
    RP (Ring Position, List of 3 Numbers from 1 - 26)
    l (Input letter)"""
    l = l.upper()  ##First I change all the letters that are inputted to an uppercase letter for simplicity and originality
    SL1, SL2, SL3 = ScramblerNum[SL[0]], ScramblerNum[SL[1]], ScramblerNum[
        SL[2]]  ## Turns the Three roman numerals of the scrambler into Numbers
    SP1, SP2, SP3 = ord(SP[0]) - 65, ord(SP[1]) - 65, ord(SP[2]) - 65
    ## Creates the 3 Scramblers with the specific information
    S1 = Scrambler(3, Scramblers[SL1], Scramblers[6][SL1], SP1, RP[0])  ##Left scrambler in the machine
    S2 = Scrambler(2, Scramblers[SL2], Scramblers[6][SL2], SP2, RP[1])  ##Middle Scrambler in the machine
    S3 = Scrambler(1, Scramblers[SL3], Scramblers[6][SL3], SP3, RP[2])  ##Right Scrambler in the machine
    BP = {value: key for key, value in PB.items()}  # Creating a Second Dictionary with the reversed keys
    ScramblerText.close()  # Important to close the File --> Otherwise it corupts
    S1.RingSetting, S2.RingSetting, S3.RingSetting

    pbo = Plugboard(l, PB, BP)
    print(pbo)
    so = S1.forward(S2.forward(S3.forward(pbo)))
    print(S1.State, S2.State, S3.State)
    rf0 = Scramblers[5][so]
    rf = S3.backward(S2.backward(S1.backward(rf0)))
    ##Checking wether the letter is in the Plugboard or not
    if rf in PB:
        pbor = PB[rf]
        return [pbor]
    elif rf in BP:
        pbor = BP[rf]
        return [pbor]
    else:
        return [rf]


class Scrambler(object):
    def __init__(self, Position, Wiring, TurnOverNotch, State, RingPosition):
        # Declaring the Variables for the class
        self.Position = Position
        self.Wiring = Wiring
        self.TurnOverNotch = TurnOverNotch
        self.State = State
        self.RingPosition = RingPosition
        self.counter = 0

    def RingSetting(self):
        c = copy(self.Wiring)
        ring = self.RingPosition - 1
        if ring == 0:
            return self.wiring
        else:
            for i in range(ring):
                for x in range(26):
                    self.Wiring[chr(i + 65)] = c[chr(((i + 1) % 26) + 65)]
            return self.Wiring

    def forward(self, letter):
        self.counter += 1
        print(self.counter)
        lnumber = ord(letter) - 65
        if self.Position == 1:
            self.State += 1
            letter_new = chr(((ord(self.Wiring[chr((lnumber + self.State) % 26 + 65)]) - 65 - self.State) % 26) + 65)
        elif self.Position == 2:
            if self.counter == ord(self.TurnOverNotch):
                self.State += 1
                letter_new = chr(
                    ((ord(self.Wiring[chr((lnumber + self.State) % 26 + 65)]) - 65 - self.State) % 26) + 65)
            else:
                letter_new = chr(
                    ((ord(self.Wiring[chr((lnumber + self.State) % 26 + 65)]) - 65 - self.State) % 26) + 65)
        elif self.Position == 3:
            if self.counter == ord(self.TurnOverNotch) + 26:
                self.State += 1
                letter_new = chr(
                    ((ord(self.Wiring[chr((lnumber + self.State) % 26 + 65)]) - 65 - self.State) % 26) + 65)
            else:
                letter_new = chr(
                    ((ord(self.Wiring[chr((lnumber + self.State) % 26 + 65)]) - 65 - self.State) % 26) + 65)
        print(letter_new)
        return letter_new

    def backward(self, letter):
        lnumber = ord(letter) - 65
        reverse = {value: key for key, value in self.Wiring.items()}
        if self.Position == 1:
            letter_new = chr(((ord(reverse[chr((lnumber + self.State) % 26 + 65)]) - 65 - self.State) % 26) + 65)
        elif self.Position == 2:
            letter_new = chr(((ord(reverse[chr((lnumber + self.State) % 26 + 65)]) - 65 - self.State) % 26) + 65)
        elif self.Position == 3:
            letter_new = chr(((ord(reverse[chr((lnumber + self.State) % 26 + 65)]) - 65 - self.State) % 26) + 65)
        print(letter_new)
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


def Reflector(l, f):
    ##Letter first goes through reflector scrambler, then back from right to left through scramblers
    l = Scramblers[5][l]
    print(l)
    ## following code is a way to flip the direction of a dictionary, pretty much checks for all the values of dict then all keys and searches for index i
    s1, s2, s3 = {value: key for key, value in f[0].items()}, {value: key for key, value in f[1].items()}, {value: key
                                                                                                            for
                                                                                                            key, value
                                                                                                            in f[
                                                                                                                2].items()}
    return s3[s2[s1[l]]]


##Changes roman numerals to Python Indices
ScramblerNum = {"I": 0, "II": 1, "III": 2, "IV": 3, "V": 4}

##Input Values
SL = ["I", "II", "III"]
SP = ["A", "B", "C"]
PB = {
    "A": "G",
    "H": "Q",
    "O": "C",
    "Z": "Y",
    "N": "M",
    "T": "K"
}
RP = [1, 1, 1]
##Call Function Enigma
for q in range(1):
    print(Enigma(SL, SP, PB, RP, "H"))
