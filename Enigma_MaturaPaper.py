def Enigma(SL, SP, PB, l):
    """SL will be a list of 3 numbers ranging from 1-3 which is the Location of the scramblers
SP will be a list of three numbers ranging from 1-26 (For letters A-Z) which is the letter on each of the Scramblers
PB will be the Plugboard setting, being a dictionary of 6 letters with their corresponding letter
l is a letter that has to be encoded with enigma"""
    l = l.upper()
    ##3 Scramblers in a row that have the 3 different positions specified in list SL
    so = Scrambler(Scrambler(Scrambler(l, SL[0]), SL[1]), SL[2])
    pbo = Plugboard(so)
    return pbo


##I will try and complete the scrambler functions using just dictionaries at this point in time it looks like it's the most plausible choice
def Scrambler(l, n):
    """Takes letter l and scrambler # (n) as input"""
    ##Here I take n which is the number of the scrambler and l which is the letter that is inputted and search for its counter part in the Scramblers list
    return Scramblers[n - 1][l]


def Plugboard(l):
    """Takes letter l and checks for it in the plugboard"""
    if l in PB:
        pbo = PB[l]
    else:
        pbo = l
    return pbo


##Test Values

Scramblers = [
    {"A": "D", "B": "M", "C": "T", "D": "W", "E": "S", "F": "I", "G": "L", "H": "R", "I": "U", "J": "Y", "K": "Q",
     "L": "N",
     "M": "K", "N": "F", "O": "E", "P": "J", "Q": "C", "R": "A", "S": "Z", "T": "B", "U": "P", "V": "G", "W": "X",
     "X": "O",
     "Y": "H", "Z": "V"},
    {"A": "H", "B": "Q", "C": "Z", "D": "G", "E": "P", "F": "J", "G": "T", "H": "M", "I": "O", "J": "B", "K": "L",
     "L": "N",
     "M": "C", "N": "I", "O": "F", "P": "D", "Q": "Y", "R": "A", "S": "W", "T": "V", "U": "E", "V": "U", "W": "S",
     "X": "R",
     "Y": "K", "Z": "X"},
    {"A": "U", "B": "Q", "C": "N", "D": "T", "E": "L", "F": "S", "G": "Z", "H": "F", "I": "M", "J": "R", "K": "E",
     "L": "H",
     "M": "D", "N": "P", "O": "X", "P": "K", "Q": "I", "R": "B", "S": "V", "T": "Y", "U": "G", "V": "J", "W": "C",
     "X": "W",
     "Y": "O", "Z": "A"}]

SL = [1, 2, 3]
SP = [26, 26, 26]
PB = {"A": "G",
      "H": "Q",
      "O": "C",
      "Z": "Y",
      "N": "M",
      "T": "K"}

##Test Area

##print(Scrambler("B", 1))
print(Enigma(SL, SP, PB, "h"))
