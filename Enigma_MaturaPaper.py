import json
from copy import *
##ScramblerWiring info is opened --> and json information extracted
ScramblerText = open('ScramblerText.txt', 'r')
Scramblers = json.load(ScramblerText)

##Main Function
def Enigma(SL, SP, PB, l):
    l = l.upper()
    print ("Input Letter:" + l)
    ##3 Scramblers in a row that have the positions and name specified in list SL (0 is left most scrambler), then Roman numerals translated into python data
    ##Plugboard function, Scrambler Function used 3 times in a row with different scramblers, Reflector then checked wether output rf is in the reverse plugboard or not
    SL1, SL2, SL3 = ScramblerNum[SL[0]], ScramblerNum[SL[1]], ScramblerNum[SL[2]]
    ##S1-S3 are the Different classes for the 3 chosen Scramblers
    S1 = Scrambler(Scramblers[SL1], Scramblers[6][SL1], SP[0])
    S2 = Scrambler(Scramblers[SL2], Scramblers[6][SL2], SP[1])
    S3 = Scrambler(Scramblers[SL3], Scramblers[6][SL3], SP[2])
    s1, s2, s3 = deepcopy(S1), deepcopy(S2), deepcopy(S3) #Copying the Scramblers so that it can be used in the beginning REDO!!!
    BP = {value: key for key, value in PB.items()} #Creating a Second Dictionary with the reversed keys
    ScramblerText.close() #Important to close the File --> Otherwise it corupts
    InitRotate([S3, S2, S1],[s3, s2, s1])
    Rotator([S3, S2, S1],[s3, s2, s1])
    pbo = Plugboard(l, PB, BP)
    print(pbo)
    so = S1.encode(S2.encode(S3.encode(l)))
    print(so)
    rf = Reflector(so,[SL1, SL2, SL3])
    print(rf)
    ##Checking wether the letter is in the Plugboard or not
    if rf in PB:
        pbor = PB[rf]
        return [pbor, [S1.State, S2.State, S3.State]]
    elif rf in BP:
        pbor = BP[rf]
        return [pbor, [S1.State, S2.State, S3.State]]
    else:
        return [rf, [S1.State, S2.State, S3.State]]

##Sub Functions
class Scrambler(object):
    def __init__(self, Wiring, TurnOverNotch, State):
        self.Wiring = Wiring
        self.TurnOverNotch = TurnOverNotch
        self.State = State

    def encode(self, letter):
        """Encodes the letter with the wiring of the Scrambler"""
        return self.Wiring[letter]

    # def InitRotate(self):
    #     c = copy(self.Wiring)
    #     for i in range(ord(self.State)):
    #         for x in range(26):
    #             self.Wiring[chr(i + 65)] = c[chr(((i + 1) % 26) + 65)]

def InitRotate(Scram, STEMP):
    """This is the Initial Rotation to the correct position set on the Enigma"""
    cp1, CP1, cp2, CP2, cp3, CP3 = Scram[0].State, STEMP[0].State, Scram[1].State, STEMP[1].State, Scram[2].State, STEMP[2].State
    S1, Stemp1, S2, Stemp2, S3, Stemp3 = Scram[0].Wiring, STEMP[0].Wiring, Scram[1].Wiring, STEMP[1].Wiring, Scram[2].Wiring, STEMP[2].Wiring
    for i in range(ord(CP1)):
        for x in range(26):
            S1[chr(i + 65)] = Stemp1[chr(((i + 1) % 26) + 65)]
    for i in range(ord(CP2)):
        for x in range(26):
            S2[chr(i + 65)] = Stemp2[chr(((i + 1) % 26) + 65)]
    for i in range(ord(CP3)):
        for x in range(26):
            S3[chr(i + 65)] = Stemp3[chr(((i + 1) % 26) + 65)]

def Plugboard(l, PB, BP):
    ##If the letter is in the Plugboard(PB) then it changes its value otherwise it keeps it.
    if l in PB:
        pbo = PB[l]
    elif l in BP:
        pbo = BP[l]
    else:
        pbo = l
    return pbo

def Rotator(Scram, STEMP):
    ##Setup of the Variables with the Variable Dictionary and the Fixed Dictionary
    cp1, CP1, cp2, CP2, cp3, CP3 = Scram[0].State, STEMP[0].State, Scram[1].State, STEMP[1].State, Scram[2].State, STEMP[2].State
    S1, Stemp1, S2, Stemp2, S3, Stemp3 = Scram[0].Wiring, STEMP[0].Wiring, Scram[1].Wiring, STEMP[1].Wiring, Scram[2].Wiring, STEMP[2].Wiring
    ##Rotation takes place
    for i in range(26):
        S1[chr(i + 65)] = Stemp1[chr(((i + 1) % 26) + 65)]
    cp1 = chr(ord(CP1) + 1)
    if cp1 == Scram[0].TurnOverNotch:
        for i in range(26):
            S2[chr(i + 65)] = Stemp2[chr(((i + 1) % 26) + 65)]
        cp2 = chr(ord(CP2) + 1)
    if cp2 == Scram[1].TurnOverNotch:
        for i in range(26):
            S3[chr(i + 65)] = Stemp3[chr(((i + 1) % 26) + 65)]
        cp3 = chr(ord(CP3) + 1)

def Reflector(l, f):
    ##Letter first goes through reflector scrambler, then back from right to left through scramblers
    l = Scramblers[5][l]
    ## following code is a way to flip the direction of a dictionary, pretty much checks for all the values of dict then all keys and searches for index i
    s1, s2, s3 = {value: key for key, value in Scramblers[f[0]].items()}, {value: key for key, value in Scramblers[f[1]].items()}, {value: key for key, value in Scramblers[f[2]].items()}
    return s3[s2[s1[l]]]


##Changes roman numerals to Python Indices
ScramblerNum = {"I":0,"II":1,"III":2,"IV":3,"V":4}

##Input Values
SL = ["I","II","III"]
SP = ["A","B","C"]
PB = {"A":"G",
      "H":"Q",
      "O":"C",
      "Z":"Y",
      "N":"M",
      "T":"K"}

##Call Function Enigma
for q in range(2):
    print(Enigma(SL, SP, PB, "A"))
