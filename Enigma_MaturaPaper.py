import json
##ScramblerWiring info is opened --> and json information extracted
ScramblerText = open('ScramblerText.txt', 'r')
Scramblers = json.load(ScramblerText)

##Main Function
def Enigma (SL, SP, PB, RP, word):
    """SL (Scrambler Location, List of 3 Scramblers)
    SP (Scrambler Position, List of 3 Letters you can see on the machine)
    PB (Plugboard, Dictionary with 0 - 13 Letters connecting with eachother)
    RP (Ring Position, List of 3 Numbers from 1 - 26)
    word (Input)"""
    ScramblerNum = {"I":0,"II":1,"III":2,"IV":3,"V":4}
    SL1, SL2, SL3 = ScramblerNum[SL[0]], ScramblerNum[SL[1]], ScramblerNum[SL[2]] ## Turns the Three roman numerals of the scrambler into Numbers
    SP1, SP2, SP3 = ord(SP[0]) - 65, ord(SP[1]) - 65, ord(SP[2]) - 65 ##Turn State into Numbers
    ## Creates the 3 Scramblers with the specific information
    S1 = Scrambler(Scramblers[SL1], Scramblers[6][SL1], SP1, RP[0]) ##Left scrambler in the machine
    S2 = Scrambler(Scramblers[SL2], Scramblers[6][SL2], SP2, RP[1]) ##Middle Scrambler in the machine
    S3 = Scrambler(Scramblers[SL3], Scramblers[6][SL3], SP3, RP[2]) ##Right Scrambler in the machine
    BP = {value: key for key, value in PB.items()} ##Creating a Second Dictionary with the reversed keys
    PB.update(BP) ##Joining Both Dictionaries
    ScramblerText.close() ##Important to close the File -->  Otherwise it corupts
    y = False ##Variables to prevent repetition
    S1.ring_setting(), S2.ring_setting(), S3.ring_setting() ##Applies ring setting

    for l in word: ##Iterates through the Script for each component of word (In this case letters)
        l = l.upper() ##All input are changed to uppercase
        pbd = plugboard(l, PB) ##Input l goes through Plugboard function with arguments l (letter) and PB (Dictionary for Plugboard)

        ##Forward through Scramblers
        S3.state_up() ##State increased by one
        letter_new1 = S3.forward(pbd)
        ##If the State Matches that of the TurnOverNotch, State of next rotor goes up by one
        if S3.State == ord(S3.TurnOverNotch) - 64:
            S2.state_up()
            y = True
        print(y)
        letter_new2 = S2.forward(letter_new1)
        if S2.State == ord(S2.TurnOverNotch) - 64 and y:
            S1.state_up()
            y = False
        letter_new3 = S1.forward(letter_new2)
        print(chr(S1.State + 65), chr(S2.State + 65), chr(S3.State + 65), end = "/")

        ##Back through Scramblers
        rf = Scramblers[5][letter_new3] ##Letter goes through Reflector Dictionary
        letter_back1 = S1.backward(rf)
        letter_back2 = S2.backward(letter_back1)
        letter_back3 = S3.backward(letter_back2)

        ##Checking whether the letter is in the Plugboard or not
        print(plugboard(letter_back3, PB))

##Scrambler Class

class Scrambler(object):
    def __init__(self, Wiring, TurnOverNotch, State, RingPosition):
        #Declaring the Variables for the class
        self.Wiring = Wiring
        self.TurnOverNotch = TurnOverNotch
        self.State = State
        self.RingPosition = RingPosition

    def ring_setting(self):
        ##Sets RingPosition to start from 0 not 1
        self.RingPosition -= 1

    def state_up(self):
        ##State goes up by one, State remains smaller than 26
        self.State += 1
        self.State %= 26

    def forward(self, l):
        ##State is added to the letter Ring Position is subtracted then checked whether it is bigger than 26
        return chr(((ord(self.Wiring[chr((ord(l) - 65 + self.State - self.RingPosition)%26 + 65)]) - 65 - self.State + self.RingPosition)% 26) + 65)

    def backward(self, l):
        og = {value: key for key, value in self.Wiring.items()}
        return chr(((ord(og[chr((ord(l) - 65 + self.State - self.RingPosition)%26 + 65)]) - 65 - self.State + self.RingPosition)% 26) + 65)

##Sub Functions

def plugboard(l, PB):
    ##If the letter is in the Plugboard(PB) then it changes its value otherwise it keeps it.
    if l in PB:
        pbo = PB[l]
    else:
        pbo = l
    return pbo

##Input Values
SL = ["I","II","III"]
SP = ["A","D","U"]
PB = {}
RP = [4,4,4]
# SL = ["I","II","III"]
# SP = ["A","A","A"]
# PB = {}
# RP = [4,4,4]
##Call Function Enigma
Enigma(SL, SP, PB, RP, "WritteninthesewallsarethestoriesthatIcantexplainIleavemyheartopenbutitstaysrighthereemptyfordaysShetoldmeinthemorningShedontfeelthesameaboutusinherbonesItseemstomethatwhenIdieThesewordswillbewrittenonmystoneAndIllbegonegonetonightThegroundbeneathmyfeetisopenwideThewaythatIvebeenholdinontootightWithnothinginbetweenThestoryofmylifeItakeherhomeIdriveallnighttokeepherwarmandtimeIsfrozenthestoryofthestoryofThestoryofmylifeIgiveherhopeIspendherloveuntilshesbrokeinsideThestoryofmylifethestoryofthestoryofWrittenonthesewallsareThecolorsthatIcantchangeLeavemyheartopenButitstaysrighthereinitscageIknowthatinthemorningnowIseeascendinglightuponahillAlthoughIambrokenmyheartisuntamedstillAndIllbegonegonetonightThefirebeneathmyfeetisburningbrightThewaythatIvebeenholdinonsotightWithnothinginbetweenThestoryofmylifeItakeherhomeIdriveallnighttokeepherwarmandtimeIsfrozenthestoryofthestoryofThestoryofmylifeIgiveherhopeIspendherloveuntilshesbrokeinsideThestoryofmylifethestoryof")
