import json

# ScramblerWiring info is opened --> and json information extracted
ScramblerText = open('ScramblerText.json', 'r')
Scramblers = json.load(ScramblerText)


# Main Function
def enigma(sl, sp, pb, rp, word):
    """sl (Scrambler Location, List of 3 Scramblers)
    sp (Scrambler Position, List of 3 Letters you can see on the machine)
    pb (Plugboard, Dictionary with 0 - 13 Letters connecting with eachother)
    rp (Ring Position, List of 3 Numbers from 1 - 26)
    word (Input)"""
    scrambler_num = {"I": 0, "II": 1, "III": 2, "IV": 3, "V": 4}
    sl1, sl2, sl3 = scrambler_num[sl[0]], scrambler_num[sl[1]], scrambler_num[sl[2]]  # Turns the Three roman numerals of the scrambler into Numbers
    sp1, sp2, sp3 = ord(sp[0]) - 65, ord(sp[1]) - 65, ord(sp[2]) - 65  # Turn State into Numbers
    # Creates the 3 Scramblers with the specific information
    S1 = Scrambler(Scramblers[sl1], Scramblers[6][sl1], sp1, rp[0])  # Left scrambler in the machine
    S2 = Scrambler(Scramblers[sl2], Scramblers[6][sl2], sp2, rp[1])  # Middle Scrambler in the machine
    S3 = Scrambler(Scramblers[sl3], Scramblers[6][sl3], sp3, rp[2])  # Right Scrambler in the machine
    BP = {value: key for key, value in pb.items()}  # Creating a Second Dictionary with the reversed keys
    pb.update(BP)  # Joining Both Dictionaries
    ScramblerText.close()  # Important to close the File -->  Otherwise it corrupts
    x, y, z = False, False, False  # Variables to prevent repetition
    S1.ring_setting(), S2.ring_setting(), S3.ring_setting()  # Applies ring setting

    for w in word:  # Iterates through the Script for each component of word (In this case letters)
        w = w.upper()  # All input are changed to uppercase
        pbd = plugboard(w, pb)  # Input l goes through Plugboard function with arguments l (letter) and pb (Dictionary for Plugboard)

        # Forward through Scramblers
        S3.state_up()  # State increased by one
        # If the State Matches that of the TurnOverNotch, State of next rotor goes up by one
        if x:
            S2.state_up()
            x = False
            z = True
        if y and z:
            S1.state_up()
            S2.state_up()
            y = False
            z = False
        letter_new1 = S3.forward(pbd)
        letter_new2 = S2.forward(letter_new1)
        letter_new3 = S1.forward(letter_new2)
        if S3.State == ord(S3.TurnOverNotch) - 65:
            x = True
        if S2.State == ord(S2.TurnOverNotch) - 65:
            y = True

        # Back through Scramblers
        rf = Scramblers[5][letter_new3]  # Letter goes through Reflector Dictionary
        letter_back1 = S1.backward(rf)
        letter_back2 = S2.backward(letter_back1)
        letter_back3 = S3.backward(letter_back2)

        # Checking whether the letter is in the Plugboard or not
        print(plugboard(letter_back3, pb), end="")


# Scrambler Class
class Scrambler(object):
    def __init__(self, wiring, turn_over_notch, state, ring_position):
        # Declaring the Variables for the class
        self.Wiring = wiring
        self.TurnOverNotch = turn_over_notch
        self.State = state
        self.RingPosition = ring_position

    def ring_setting(self):
        # Sets RingPosition to start from 0 not 1
        self.RingPosition -= 1

    def state_up(self):
        # State goes up by one, State remains smaller than 26
        self.State += 1
        self.State %= 26

    def forward(self, l):
        # State is added to the letter Ring Position is subtracted then checked whether it is bigger than 26
        return chr(((ord(self.Wiring[chr((ord(l) - 65 + self.State - self.RingPosition) % 26 + 65)]) - 65 - self.State + self.RingPosition) % 26) + 65)

    def backward(self, l):
        og = {value: key for key, value in self.Wiring.items()}
        return chr(((ord(og[chr((ord(l) - 65 + self.State - self.RingPosition) % 26 + 65)]) - 65 - self.State + self.RingPosition) % 26) + 65)


# Sub Functions
def plugboard(l, pb):
    # If the letter is in the Plugboard(pb) then it changes its value otherwise it keeps it.
    if l in pb:
        pbo = pb[l]
    else:
        pbo = l
    return pbo


# Input Values
SL = ["I", "IV", "II"]
SP = ["A", "R", "Y"]
PB = {
    "A": "C",
    "B": "Q",
    "E": "T",
    "G": "Y",
    "I": "R",
    "J": "W",
    "L": "S",
    "M": "U",
    "N": "O",
    "X": "Z"
}
RP = [7, 11, 19]
word_input = "helloxmeetxmexatxthexstairs"
# Call Function Enigma
enigma(SL, SP, PB, RP, word_input)
