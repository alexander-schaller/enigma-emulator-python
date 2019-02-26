import json
##Scrambler #1 turns over between Q and R, Scrambler #2 turns over between E and F, Scrambler #3 turns over between V and W
##Scramblers are saved as .txt documents, here they're opened
ScramblerText = open('ScramblerText.txt', 'r')
Scramblers = json.load(ScramblerText)
def Enigma(SL, SP, PB, l):
    """SL will be a list of 3 numbers ranging from 1-3 which is the Location of the scramblers
SP will be a list of three numbers ranging from 1-26 (For letters A-Z) which is the letter on each of the Scramblers
PB will be the Plugboard setting, being a dictionary of 6 letters with their corresponding letter
l is a letter that has to be encoded with enigma"""
    l = l.upper()
    ##3 Scramblers in a row that have the positions specified in list SL (0 is left most scrambler)
    SL1, SL2, SL3 = SL[0], SL[1], SL[2]
    print (SL1, SL2, SL3)
    S1, S2, S3 = ScramblerNum[SL[0]], ScramblerNum[SL[1]], ScramblerNum[SL[2]]
    pbo = Plugboard(l)
    so = Scrambler(Scrambler(Scrambler(pbo, S3), S2), S1)
    rf = Reflector(so,[S1, S2, S3])
    if rf in PB.values():
        pbor = list(PB.keys())[list(PB.values()).index(rf)]
        return pbor
    else:
        return rf


##I will try and complete the scrambler functions using just dictionaries at this point in time it looks like it's the most plausible choice
def Scrambler(l,n):
    """Takes letter l and scrambler # (n) as input"""
    ##Here I take n which is the number of the scrambler and l which is the letter that is inputted and search for its counter part in the Scramblers list
    return Scramblers[n][l]

def Plugboard(l):
    """Takes letter l and checks for it in the plugboard"""
    if l in PB:
        pbo = PB[l]
    else:
        pbo = l
    return pbo

def Reflector(l, f):
    l = Scramblers[5][l]
    s1 = list(Scramblers[f[0]].keys())[list(Scramblers[f[0]].values()).index(l)]
    s2 = list(Scramblers[f[1]].keys())[list(Scramblers[f[1]].values()).index(s1)]
    s3 = list(Scramblers[f[2]].keys())[list(Scramblers[f[2]].values()).index(s2)]
    return s3

ScramblerNum = {"I":0,"II":1,"III":2,"IV":3,"V":4}
##Test Values

SL = ["I","II","III"]
SP = ["A","B","C"]
PB = {"A":"G",
      "H":"Q",
      "O":"C",
      "Z":"Y",
      "N":"M",
      "T":"K"}

##Test Area

##print(Scrambler("B", 1))
##Reflector("I",SL)
print(Enigma(SL, SP, PB, "v"))
ScramblerText.close()
