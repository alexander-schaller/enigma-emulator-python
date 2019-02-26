import json
I = "EKMFLGDQVZNTOWYHXUSPAIBRCJ"
II = "AJDKSIRUXBLHWTMCQGZNPYFVOE"
III = "BDFHJLCPRTXVZNYEIWGAKMUSQO"
IV = "ESOVPZJAYQUIRHXLNFTGKDCMWB"
V = "VZBRGITYUPSDNHLXAWMJQOFECK"
UKWB = "YRUHQSLDPXNGOKMIEBFZCWVJAT"
z = [{"A":"D","B":"M","C":"T","D":"W","E":"S","F":"I","G":"L","H":"R","I":"U","J":"Y","K":"Q","L":"N",
    "M":"K","N":"F","O":"E","P":"J","Q":"C","R":"A","S":"Z","T":"B","U":"P","V":"G","W":"X","X":"O",
    "Y":"H","Z":"V"},
    {"A":"H","B":"Q","C":"Z","D":"G","E":"P","F":"J","G":"T","H":"M","I":"O","J":"B","K":"L","L":"N",
    "M":"C","N":"I","O":"F","P":"D","Q":"Y","R":"A","S":"W","T":"V","U":"E","V":"U","W":"S","X":"R",
    "Y":"K","Z":"X"},
    {"A":"U","B":"Q","C":"N","D":"T","E":"L","F":"S","G":"Z","H":"F","I":"M","J":"R","K":"E","L":"H",
    "M":"D","N":"P","O":"X","P":"K","Q":"I","R":"B","S":"V","T":"Y","U":"G","V":"J","W":"C","X":"W",
    "Y":"O","Z":"A"},
    {"A":"H","B":"Q","C":"Z","D":"G","E":"P","F":"J","G":"T","H":"M","I":"O","J":"B","K":"L","L":"N",
    "M":"C","N":"I","O":"F","P":"D","Q":"Y","R":"A","S":"W","T":"V","U":"E","V":"U","W":"S","X":"R",
    "Y":"K","Z":"X"},
    {"A":"H","B":"Q","C":"Z","D":"G","E":"P","F":"J","G":"T","H":"M","I":"O","J":"B","K":"L","L":"N",
    "M":"C","N":"I","O":"F","P":"D","Q":"Y","R":"A","S":"W","T":"V","U":"E","V":"U","W":"S","X":"R",
    "Y":"K","Z":"X"},
    {"A":"H","B":"Q","C":"Z","D":"G","E":"P","F":"J","G":"T","H":"M","I":"O","J":"B","K":"L","L":"N",
    "M":"C","N":"I","O":"F","P":"D","Q":"Y","R":"A","S":"W","T":"V","U":"E","V":"U","W":"S","X":"R",
    "Y":"K","Z":"X"}
    ]
for i in range(1,27):
    l = chr(i+64)
    z[0][l] = I[i-1]
    z[1][l] = II[i-1]
    z[2][l] = III[i-1]
    z[3][l] = IV[i-1]
    z[4][l] = V[i-1]
    z[5][l] = UKWB[i-1]

s = open('ScramblerText.txt', 'r+')
json.dump(z, s)

s.close()
