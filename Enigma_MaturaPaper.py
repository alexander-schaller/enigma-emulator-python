import json
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

##ScramblerWiring info is opened --> and json information extracted
ScramblerText = open('ScramblerText.txt', 'r')
Scramblers = json.load(ScramblerText)


##Main Function
def Enigma(*args):
    """SL (Scrambler Location, List of 3 Scramblers)
    SP (Scrambler Position, List of 3 Letters you can see on the machine)
    PB (Plugboard, Dictionary with 0 - 13 Letters connecting with eachother)
    RP (Ring Position, List of 3 Numbers from 1 - 26)
    word (Input)"""
    try:
        SL = [sl1.get(), sl2.get(), sl3.get()]
        SP = [sp1.get(), sp2.get(), sp3.get()]
        PB = {
            "B": "O",
            "C": "W",
            "D": "Y",
            "F": "P",
            "G": "R",
            "H": "K",
            "I": "U",
            "L": "S",
            "M": "N",
            "Q": "V"
        }
        RP = [int(rp1.get()), int(rp2.get()), int(rp3.get())]
        word = WORD.get()
        ScramblerNum = {"I": 0, "II": 1, "III": 2, "IV": 3, "V": 4}
        SL1, SL2, SL3 = ScramblerNum[SL[0]], ScramblerNum[SL[1]], ScramblerNum[
            SL[2]]  ## Turns the Three roman numerals of the scrambler into Numbers
        SP1, SP2, SP3 = ord(SP[0]) - 65, ord(SP[1]) - 65, ord(SP[2]) - 65  ##Turn State into Numbers
        ## Creates the 3 Scramblers with the specific information
        S1 = Scrambler(Scramblers[SL1], Scramblers[6][SL1], SP1, RP[0])  ##Left scrambler in the machine
        S2 = Scrambler(Scramblers[SL2], Scramblers[6][SL2], SP2, RP[1])  ##Middle Scrambler in the machine
        S3 = Scrambler(Scramblers[SL3], Scramblers[6][SL3], SP3, RP[2])  ##Right Scrambler in the machine
        BP = {value: key for key, value in PB.items()}  ##Creating a Second Dictionary with the reversed keys
        PB.update(BP)  ##Joining Both Dictionaries
        ScramblerText.close()  ##Important to close the File -->  Otherwise it corupts
        x, y, z = False, False, False  ##Variables to prevent repetition
        S1.ring_setting(), S2.ring_setting(), S3.ring_setting()  ##Applies ring setting
        a = ""

        for l in word:  ##Iterates through the Script for each component of word (In this case letters)
            l = l.upper()  ##All input are changed to uppercase
            pbd = plugboard(l,
                            PB)  ##Input l goes through Plugboard function with arguments l (letter) and PB (Dictionary for Plugboard)

            ##Forward through Scramblers
            S3.state_up()  ##State increased by one
            ##If the State Matches that of the TurnOverNotch, State of next rotor goes up by one
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

            ##Back through Scramblers
            rf = Scramblers[5][letter_new3]  ##Letter goes through Reflector Dictionary
            letter_back1 = S1.backward(rf)
            letter_back2 = S2.backward(letter_back1)
            letter_back3 = S3.backward(letter_back2)

            ##Checking whether the letter is in the Plugboard or not
            a += plugboard(letter_back3, PB)

        Output.set(a)

    except:
        messagebox.showinfo(parent=content, icon='warning', message='Incorrect Input')
        Scrambler1_SP.delete(0, 'end')
        Scrambler2_SP.delete(0, 'end')
        Scrambler3_SP.delete(0, 'end')
        Scrambler1_RP.delete(0, 'end')
        Scrambler2_RP.delete(0, 'end')
        Scrambler3_RP.delete(0, 'end')
        textinput.delete(0, 'end')


##Scrambler Class
class Scrambler(object):
    def __init__(self, Wiring, TurnOverNotch, State, RingPosition):
        # Declaring the Variables for the class
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
        return chr(((ord(self.Wiring[chr((ord(
            l) - 65 + self.State - self.RingPosition) % 26 + 65)]) - 65 - self.State + self.RingPosition) % 26) + 65)

    def backward(self, l):
        og = {value: key for key, value in self.Wiring.items()}
        return chr(((ord(og[chr((ord(
            l) - 65 + self.State - self.RingPosition) % 26 + 65)]) - 65 - self.State + self.RingPosition) % 26) + 65)


##Sub Functions
def plugboard(l, PB):
    ##If the letter is in the Plugboard(PB) then it changes its value otherwise it keeps it.
    if l in PB:
        pbo = PB[l]
    else:
        pbo = l
    return pbo


def validate():
    if len(str(sp1.get())) > 0:
        return False
    ##    elif str(sp1.get()).isdigit:
    ##        return False
    else:
        return True


def invalid(event=None):
    Scrambler1_SP.delete('end')


root = Tk()
root.title("Enigma Emulator")
content = ttk.Frame(root, padding="3 3 12 12")
content.grid(column=0, row=0, sticky=(N, W, E, S))
content.columnconfigure(0, weight=1)
content.rowconfigure(0, weight=1)

Output = StringVar()
sl1 = StringVar()
sl2 = StringVar()
sl3 = StringVar()
sp1 = StringVar()
sp2 = StringVar()
sp3 = StringVar()
pb = StringVar()
rp1 = StringVar()
rp2 = StringVar()
rp3 = StringVar()
WORD = StringVar()

label1 = ttk.Label(content, text="Results", justify='center')
label1.grid(column=3, row=10)
label1['textvariable'] = Output

label2 = ttk.Label(content, text="Scrambler:")
label2.grid(column=1, row=2, sticky=(W, E))
label3 = ttk.Label(content, text="Window:")
label3.grid(column=1, row=3, sticky=(W, E))
label4 = ttk.Label(content, text="Ring:")
label4.grid(column=1, row=4, sticky=(W, E))
label5 = ttk.Label(content, text="Plugboard:", justify='center')
label5.grid(column=3, row=5)

label6 = ttk.Label(content, text="Left Scrambler", justify='center')
label6.grid(column=2, row=1, columnspan=10, sticky=(W, E))
Scrambler1_SL = ttk.Combobox(content, textvariable=sl1, width=10, state="readonly")
Scrambler1_SL.grid(column=2, row=2)
Scrambler1_SL['values'] = ('I', 'II', 'III', 'IV', 'V')
Scrambler1_SL.current(0)
Scrambler1_SP = ttk.Entry(content, textvariable=sp1, width=10, validate='all', validatecommand=validate,
                          invalidcommand=invalid)
Scrambler1_SP.grid(column=2, row=3)
Scrambler1_SP.bind("<BackSpace>", invalid)
Scrambler1_RP = ttk.Entry(content, textvariable=rp1, width=10)
Scrambler1_RP.grid(column=2, row=4)

label7 = ttk.Label(content, text="Middle Scrambler", justify='center')
label7.grid(column=3, row=1, columnspan=10, sticky=(W))
Scrambler2_SL = ttk.Combobox(content, textvariable=sl2, width=10, state="readonly")
Scrambler2_SL.grid(column=3, row=2)
Scrambler2_SL['values'] = ('I', 'II', 'III', 'IV', 'V')
Scrambler2_SL.current(1)
Scrambler2_SP = ttk.Entry(content, textvariable=sp2, width=10)
Scrambler2_SP.grid(column=3, row=3)
Scrambler2_RP = ttk.Entry(content, textvariable=rp2, width=10)
Scrambler2_RP.grid(column=3, row=4)

label8 = ttk.Label(content, text="Right Scrambler", justify='center')
label8.grid(column=4, row=1, columnspan=10, sticky=(W))
Scrambler3_SL = ttk.Combobox(content, textvariable=sl3, width=10, state="readonly")
Scrambler3_SL.grid(column=4, row=2)
Scrambler3_SL['values'] = ('I', 'II', 'III', 'IV', 'V')
Scrambler3_SL.current(2)
Scrambler3_SP = ttk.Entry(content, textvariable=sp3, width=10)
Scrambler3_SP.grid(column=4, row=3)
Scrambler3_RP = ttk.Entry(content, textvariable=rp3, width=10)
Scrambler3_RP.grid(column=4, row=4)

textinput = ttk.Entry(content, textvariable=WORD, width=10)
textinput.grid(column=3, row=8)

button = ttk.Button(content, text='Run', command=Enigma)
button.grid(column=3, row=9)

menubar = Menu(root)
appmenu = Menu(menubar, name='apple')
menubar.add_cascade(menu=appmenu)
appmenu.add_command(label='Enigma Emulator')
appmenu.add_separator()
root['menu'] = menubar

runmenu = Menu(menubar, name='run')
menubar.add_cascade(menu=runmenu, label='Run')
runmenu.add_command(command=Enigma, label='Run Enigma Emulator')

windowmenu = Menu(menubar, name='window')
menubar.add_cascade(menu=windowmenu, label='Window')

root.mainloop()
