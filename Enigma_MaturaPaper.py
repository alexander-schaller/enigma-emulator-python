import json
##ScramblerWiring info is opened --> and json information extracted
ScramblerText = open('ScramblerText.txt', 'r')
Scramblers = json.load(ScramblerText)

##Main Function
def Enigma(SL, SP, IR, PB, l):
    """SL will be a list of 3 numbers ranging from 1-3 which is the Location of the scramblers
    SP will be a list of three numbers ranging from 1-26 (For letters A-Z) which is the letter on each of the Scramblers
    IR is the setting of the Index Ring
    PB will be the Plugboard setting, being a dictionary of 6 letters with their corresponding letter
    l is a letter that has to be encoded with enigma"""
    l = l.upper()
    print ("Input Letter:" + l)
    ##3 Scramblers in a row that have the positions and name specified in list SL (0 is left most scrambler), then Roman numerals translated into python data
    SL1, SL2, SL3 = SL[0], SL[1], SL[2]
    ##Plugboard function, Scrambler Function used 3 times in a row with different scramblers, Reflector then checked wether output rf is in the reverse plugboard or not
    S1, S2, S3 = ScramblerNum[SL[0]], ScramblerNum[SL[1]], ScramblerNum[SL[2]]
    Rotator(SL, SP)
    pbo = Plugboard(l)
    so = Scrambler(Scrambler(Scrambler(pbo, S3), S2), S1)
    rf = Reflector(so,[S1, S2, S3])
    if rf in PB.values():
        pbor = list(PB.keys())[list(PB.values()).index(rf)]
        ScramblerText.close()
        return pbor
    else:
        ScramblerText.close()
        return rf


##Sub Functions
def Scrambler(l,n):
    """Takes letter l and scrambler # (n) as input"""
    ##Here I take n which is the number of the scrambler and l which is the letter that is inputted and search for its counter part in the Scramblers list
    return Scramblers[n][l]

def Plugboard(l):
    """Takes letter l and checks for it in the plugboard"""
    ##If the letter is in the Plugboard(PB) then it changes its value otherwise it keeps it.
    if l in PB:
        pbo = PB[l]
    else:
        pbo = l
    return pbo

def Rotator(SL, cp):
    """F is the Scrambler Layout, while cp is is the current position of the scrambler"""
    ##cp is there to be used with the notch so it can turn at an apropriate position
    ##ton is equal to the turnover notch
    ton = ["Q","E","V","J","Z"]
    S1, S2, S3 = ScramblerNum[SL[0]], ScramblerNum[SL[1]], ScramblerNum[SL[2]]
    ##logic behind this is that if it reaches the turnover notch it makes the wheel turn, therefore making the next wheel move once
    s1 = Scramblers[S1]["A"]
    s2 = Scramblers[S2]["A"]
    s3 = Scramblers[S3]["A"]
    ##work with modulo in numbers 26
    for i in range(25):
        if i < 25:
            Scramblers[S1][chr(i + 65)] = Scramblers[S1][chr(i + 66)]
        else:
            Scramblers[S1][chr(i + 65)] = s1
    return Scramblers[S1]
    if cp[0] == ton[f[0]] :
        for i in range(26):
            if i < 25:
                Scramblers[S2][chr(i + 65)] = Scramblers[S2][chr(i + 66)]
            else:
                Scramblers[S2][chr(i + 65)] = s2
    if cp[1] == ton[f[1]] :
        for i in range(26):
            if i < 25:
                Scramblers[S3][chr(i + 65)] = Scramblers[S3][chr(i + 6)]
            else:
                Scramblers[S3][chr(i + 65)] = s3


def Reflector(l, f):
    """Letter l and Scrambler list f"""
    ##Letter first goes through reflector scrambler, then back from right to left through scramblers
    l = Scramblers[5][l]
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
IR = 0

##Call Function Enigma
print("Output Letter: " + Enigma(SL, SP, IR, PB, "t"))
