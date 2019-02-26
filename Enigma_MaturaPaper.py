import json
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
    # S1-S3 are the Different classes for the 3 chosen Scramblers
    S1 = Scrambler(Scramblers[SL1], Scramblers[6][SL1], SP[0])
    S2 = Scrambler(Scramblers[SL2], Scramblers[6][SL2], SP[1])
    S3 = Scrambler(Scramblers[SL3], Scramblers[6][SL3], SP[2])
    ScramblerText.close()
    Rotator([S1, S2, S3])
    pbo = Plugboard(l)
    so = S3.encode(S2.encode(S1.encode(l)))
    rf = Reflector(so,[SL1, SL2, SL3])
    if rf in PB.values():
        pbor = list(PB.keys())[list(PB.values()).index(rf)]
        return pbor
    else:
        return rf

##Sub Functions
class Scrambler(object):
    def __init__(self, Wiring, TurnOverNotch, State):
        self.Wiring = Wiring
        self.TurnOverNotch = TurnOverNotch
        self.State = State

    def encode(self, letter):
        return self.Wiring[letter]

def Plugboard(l):
    ##If the letter is in the Plugboard(PB) then it changes its value otherwise it keeps it.
    if l in PB:
        pbo = PB[l]
    else:
        pbo = l
    return pbo

def Rotator(Scram):
    cp1, cp2, cp3 = Scram[0].State, Scram[1].State, Scram[2].State
    S1, S2, S3 = Scram[0].Wiring, Scram[1].Wiring, Scram[2].Wiring
    print(cp1, cp2, cp3)
    for i in range(26):
        S1[chr((i % 26) + 65)] = S1[chr(((i + 1) % 26) + 65)]
    if cp1 == Scram[0].TurnOverNotch:
        for i in range(26):
            S2[chr((i % 26) + 65)] = S2[chr(((i + 1) % 26) + 65)]
    if cp2 == Scram[1].TurnOverNotch:
        for i in range(26):
            S3[chr((i % 26) + 65)] = S3[chr(((i + 1) % 26) + 65)]

def Reflector(l, f):
    ##Letter first goes through reflector scrambler, then back from right to left through scramblers
    l = Scramblers[5][l]
    print(l)
    ## following code is a way to flip the direction of a dictionary, pretty much checks for all the values of dict then all keys and searches for index i
    s1 = list(Scramblers[f[0]].keys())[list(Scramblers[f[0]].values()).index(l)]
    s2 = list(Scramblers[f[1]].keys())[list(Scramblers[f[1]].values()).index(s1)]
    s3 = list(Scramblers[f[2]].keys())[list(Scramblers[f[2]].values()).index(s2)]
    return s3


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
for i in "Hello":
    print("Output Letter: " + Enigma(SL, SP, PB, i))
# for q in range(100):
#     print(Enigma(SL, SP, PB, "A"))
