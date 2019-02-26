def Enigma(SL, SP, PB, l):
    """SL will be a list of 3 numbers ranging from 1-3 which is the Location of the scramblers
SP will be a list of three numbers ranging from 1-26 (For letters A-Z) which is the letter on each of the Scramblers
PB will be the Plugboard setting, being a dictionary of 6 letters with their corresponding letter
l is a letter that has to be encoded with enigma"""
    ##3 Scramblers in a row that have the 3 different positions specified in list SL
    so = Scrambler(Scrambler(Scrambler(l, SL[0]), SL[1]), SL[2])
    return so

##I will try and complete the scrambler functions using just dictionaries at this point in time it looks like it's the most plausible choice
def Scrambler(l,n):
    """Takes letter l and scrambler # (n) as input"""
    ##Here I take n which is the number of the scrambler and l which is the letter that is inputted and search for its counter part in the Scramblers list
    return Scramblers[n - 1][l]
        
##Test Values

Scramblers = [{"A":"A","B":"B","C":"C","D":"D","E":"E","F":"F","G":"G","H":"H","I":"I","J":"J","K":"K","L":"L",
    "M":"M","N":"N","O":"O","P":"P","Q":"Q","R":"R","S":"S","T":"T","U":"U","V":"V","W":"W","X":"X",
    "Y":"Y","Z":"Z"},
              {"A":"A","B":"B","C":"C","D":"D","E":"E","F":"F","G":"G","H":"H","I":"I","J":"J","K":"K","L":"L",
    "M":"M","N":"N","O":"O","P":"P","Q":"Q","R":"R","S":"S","T":"T","U":"U","V":"V","W":"W","X":"X",
    "Y":"Y","Z":"Z"},
              {"A":"A","B":"B","C":"C","D":"D","E":"E","F":"F","G":"G","H":"H","I":"I","J":"J","K":"K","L":"L",
    "M":"M","N":"N","O":"O","P":"P","Q":"Q","R":"R","S":"S","T":"T","U":"U","V":"V","W":"W","X":"X",
    "Y":"Y","Z":"Z"}]

SL = [1,2,3]
SP = [26,26,26]
PB = {"A":"A",
      "B":"B",
      "C":"C",
      "D":"D",
      "E":"E",
      "F":"F"}

##Test Area

##print(Scrambler("B", 1))
print(Enigma(SL, SP, PB, "H"))
