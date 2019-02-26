import json
I = "EKMFLGDQVZNTOWYHXUSPAIBRCJ"
II = "AJDKSIRUXBLHWTMCQGZNPYFVOE"
III = "BDFHJLCPRTXVZNYEIWGAKMUSQO"
IV = "ESOVPZJAYQUIRHXLNFTGKDCMWB"
V = "VZBRGITYUPSDNHLXAWMJQOFECK"
UKWB = "YRUHQSLDPXNGOKMIEBFZCWVJAT"
TON = ["Q","E","V","J","Z"]

st = {0 : I, 1 : II, 2 : III, 3 : IV, 4 : V, 5 : UKWB}
a = [{chr(i + 65):st[x][i] for i in range(0,26)} for x in range(0,6)]
a.append(TON)

s = open('ScramblerText.json', 'r+')
json.dump(a, s)
s.close()
