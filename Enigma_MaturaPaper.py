import tkinter as tk
import re
from tkinter import ttk
from tkinter import messagebox


class EnigmaIApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        tk.Tk.wm_title(self, "Enigma I")
        container = ttk.Frame(self, padding="3 3 12 12")
        global Stepup

        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        menubar = tk.Menu(container)
        appmenu = tk.Menu(menubar, name='apple')
        menubar.add_cascade(menu=appmenu)
        appmenu.add_command(label='Enigma Emulator')
        appmenu.add_separator()
        tk.Tk.config(self, menu=menubar)

        runmenu = tk.Menu(menubar, name='run')
        menubar.add_cascade(menu=runmenu, label='Run')
        runmenu.add_command(command=lambda: Emulator.run(Emulator), label='Run Enigma Emulator')

        windowmenu = tk.Menu(menubar, name='window')
        menubar.add_cascade(menu=windowmenu, label='Window')

        self.frames = {}

        frame = Emulator(container, self)

        self.frames[Emulator] = frame

        frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(Emulator)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class Emulator(ttk.Frame):

    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
        self.columnconfigure(3, weight=1)
        self.columnconfigure(4, weight=1)

        self.Output = tk.StringVar()
        self.Word = tk.StringVar()
        self.PB = tk.StringVar()
        self.RP = tk.StringVar()
        self.sl1, self.sl2, self.sl3 = tk.StringVar(), tk.StringVar(), tk.StringVar()
        self.sp1, self.sp2, self.sp3 = tk.StringVar(), tk.StringVar(), tk.StringVar()
        self.rp1, self.rp2, self.rp3 = tk.StringVar(), tk.StringVar(), tk.StringVar()

        label7 = ttk.Label(self, text="Scrambler #", justify='center')
        label7.grid(column=1, row=3, columnspan=5, sticky='we')

        label3 = ttk.Label(self, text="Left Scrambler", justify='center')
        label3.grid(column=2, row=2, columnspan=12, sticky='we', padx='5')
        Scrambler1_SL = ttk.Combobox(self, textvariable=self.sl1, width=10, values=('I', 'II', 'III', 'IV', 'V'),
                                     state="readonly")
        Scrambler1_SL.grid(column=2, row=3, columnspan=12, sticky='w', padx='5')
        Scrambler1_SL.current(0)

        label4 = ttk.Label(self, text="Middle Scrambler", justify='center')
        label4.grid(column=3, row=2, columnspan=12, sticky='we', padx='5')
        Scrambler2_SL = ttk.Combobox(self, textvariable=self.sl2, width=10, values=('I', 'II', 'III', 'IV', 'V'),
                                     state="readonly")
        Scrambler2_SL.grid(column=3, row=3, columnspan=12, sticky='w', padx='5')
        Scrambler2_SL.current(1)

        label5 = ttk.Label(self, text="Right Scrambler", justify='center')
        label5.grid(column=4, row=2, columnspan=12, sticky='we', padx='5')
        Scrambler3_SL = ttk.Combobox(self, textvariable=self.sl3, width=10, values=('I', 'II', 'III', 'IV', 'V'),
                                     state="readonly")
        Scrambler3_SL.grid(column=4, row=3, columnspan=12, sticky='w', padx='5')
        Scrambler3_SL.current(2)

        label6 = ttk.Label(self, text="Window", justify='center')
        label6.grid(column=1, row=4, columnspan=5, sticky='we')

        self.Scrambler1_SP = ttk.Combobox(self, textvariable=self.sp1, width=10, values=[chr(x) for x in range(65, 91)],
                                          state="readonly")
        self.Scrambler1_SP.grid(column=2, row=4, columnspan=12, sticky='w', padx='5')
        self.Scrambler1_SP.current(0)

        self.Scrambler2_SP = ttk.Combobox(self, textvariable=self.sp2, width=10, values=[chr(x) for x in range(65, 91)],
                                          state="readonly")
        self.Scrambler2_SP.grid(column=3, row=4, columnspan=12, sticky='w', padx='5')
        self.Scrambler2_SP.current(1)

        self.Scrambler3_SP = ttk.Combobox(self, textvariable=self.sp3, width=10, values=[chr(x) for x in range(65, 91)],
                                          state="readonly")
        self.Scrambler3_SP.grid(column=4, row=4, columnspan=12, sticky='w', padx='5')
        self.Scrambler3_SP.current(2)

        label8 = ttk.Label(self, text="Ring Position", justify='center')
        label8.grid(column=1, row=5, columnspan=5, sticky='we')

        Scrambler1_RP = ttk.Combobox(self, textvariable=self.rp1, width=10, values=[x for x in range(1, 27)],
                                     state="readonly")
        Scrambler1_RP.grid(column=2, row=5, columnspan=12, sticky='w', padx='5')
        Scrambler1_RP.current(0)

        Scrambler2_RP = ttk.Combobox(self, textvariable=self.rp2, width=10, values=[x for x in range(1, 27)],
                                     state="readonly")
        Scrambler2_RP.grid(column=3, row=5, columnspan=12, sticky='w', padx='5')
        Scrambler2_RP.current(0)

        Scrambler3_RP = ttk.Combobox(self, textvariable=self.rp3, width=10, values=[x for x in range(1, 27)],
                                     state="readonly")
        Scrambler3_RP.grid(column=4, row=5, columnspan=12, sticky='w', padx='5')
        Scrambler3_RP.current(0)

        label9 = ttk.Label(self, text="Plugboard", justify='center')
        label9.grid(column=1, row=6, columnspan=5, sticky='we')

        entrytext1 = ttk.Entry(self, textvariable=self.PB, width=60)
        entrytext1.grid(column=2, row=6, columnspan=60, sticky='w')

        label1 = ttk.Label(self, text="Enigma 1 Emulator")
        label1.grid(column=1, row=1, columnspan=10, sticky='we')

        s = ttk.Separator(self, orient='horizontal')
        s.grid(row=7, columnspan=10)

        self.entrytext = ttk.Entry(self, textvariable=self.Word, width=30)
        self.entrytext.grid(column=1, row=8, columnspan=30, sticky='w')

        button2 = ttk.Button(self, text="Run",
                             command=lambda: self.run())
        button2.grid(column=2, row=9)

        button3 = ttk.Button(self, text="Clear", command=self.clear)
        button3.grid(column=3, row=9)

        label2 = ttk.Label(self, wraplength=250, textvariable=self.Output, anchor="w", justify='left')
        label2.grid(column=3, row=8, columnspan=4000, sticky='w')

    def clear(self):
        self.Output.set("")
        self.entrytext.delete(0, 'end')

    def stepup(self):
        self.Scrambler1_SP.current(self.sp1.get())
        self.Scrambler2_SP.current(self.sp2.get())
        self.Scrambler3_SP.current(self.sp3.get())

    def run(self):
        try:
            self.Enigma()
            self.stepup()
        except:
            if messagebox.showerror(message='An Error occured please try again!', icon='error', title='Error Message'):
                self.clear()

    ##Main Function
    def Enigma(self):
        """SL (Scrambler Location, List of 3 Scramblers)
        SP (Scrambler Position, List of 3 Letters you can see on the machine)
        PB (Plugboard, Dictionary with 0 - 13 Letters connecting with eachother)
        RP (Ring Position, List of 3 Numbers from 1 - 26)
        word (Input)"""
        word = self.Word.get()
        Scramblers = [
            {"N": "W", "K": "N", "J": "Z", "M": "O", "C": "M", "Q": "X", "A": "E", "R": "U", "X": "R", "Z": "J",
             "P": "H", "F": "G", "G": "D", "T": "P", "S": "S", "W": "B", "D": "F", "E": "L", "I": "V", "O": "Y",
             "V": "I", "U": "A", "H": "Q", "L": "T", "B": "K", "Y": "C"},
            {"N": "T", "K": "L", "J": "B", "M": "W", "C": "D", "Q": "Q", "A": "A", "R": "G", "X": "V", "Z": "E",
             "P": "C", "F": "I", "G": "R", "T": "N", "S": "Z", "W": "F", "D": "K", "E": "S", "I": "X", "O": "M",
             "V": "Y", "U": "P", "H": "U", "L": "H", "B": "J", "Y": "O"},
            {"N": "N", "K": "X", "J": "T", "M": "Z", "C": "F", "Q": "I", "A": "B", "R": "W", "X": "S", "Z": "O",
             "P": "E", "F": "L", "G": "C", "T": "A", "S": "G", "W": "U", "D": "H", "E": "J", "I": "R", "O": "Y",
             "V": "M", "U": "K", "H": "P", "L": "V", "B": "D", "Y": "Q"},
            {"N": "H", "K": "U", "J": "Q", "M": "R", "C": "O", "Q": "N", "A": "E", "R": "F", "X": "M", "Z": "B",
             "P": "L", "F": "Z", "G": "J", "T": "G", "S": "T", "W": "C", "D": "V", "E": "P", "I": "Y", "O": "X",
             "V": "D", "U": "K", "H": "A", "L": "I", "B": "S", "Y": "W"},
            {"N": "H", "K": "S", "J": "P", "M": "N", "C": "B", "Q": "A", "A": "V", "R": "W", "X": "E", "Z": "K",
             "P": "X", "F": "I", "G": "T", "T": "J", "S": "M", "W": "F", "D": "R", "E": "G", "I": "U", "O": "L",
             "V": "O", "U": "Q", "H": "Y", "L": "D", "B": "Z", "Y": "C"},
            {"N": "K", "K": "N", "J": "X", "M": "O", "C": "U", "Q": "E", "A": "Y", "R": "B", "X": "J", "Z": "T",
             "P": "I", "F": "S", "G": "L", "T": "Z", "S": "F", "W": "V", "D": "H", "E": "Q", "I": "P", "O": "M",
             "V": "W", "U": "C", "H": "D", "L": "G", "B": "R", "Y": "A"}, ["Q", "E", "V", "J", "Z"]]
        pb = self.PB.get()
        pb = pb.upper()
        pb = pb.replace(" ", "")
        PB = {pb[x]: pb[x + 1] for x in range(0, len(pb), 2)}
        ScramblerNum = {"I": 0, "II": 1, "III": 2, "IV": 3, "V": 4}
        SL1, SL2, SL3 = ScramblerNum[self.sl1.get()], ScramblerNum[self.sl2.get()], ScramblerNum[
            self.sl3.get()]  ## Turns the Three roman numerals of the scrambler into Numbers
        SP1, SP2, SP3 = ord(self.sp1.get()) - 65, ord(self.sp2.get()) - 65, ord(
            self.sp3.get()) - 65  ##Turn State into Numbers
        ## Creates the 3 Scramblers with the specific information
        S1 = self.Scrambler(Scramblers[SL1], Scramblers[6][SL1], SP1,
                            int(self.rp1.get()))  ##Left scrambler in the machine
        S2 = self.Scrambler(Scramblers[SL2], Scramblers[6][SL2], SP2,
                            int(self.rp2.get()))  ##Middle Scrambler in the machine
        S3 = self.Scrambler(Scramblers[SL3], Scramblers[6][SL3], SP3,
                            int(self.rp3.get()))  ##Right Scrambler in the machine
        BP = {value: key for key, value in PB.items()}  ##Creating a Second Dictionary with the reversed keys
        PB.update(BP)  ##Joining Both Dictionaries
        x, y, z = False, False, False  ##Variables to prevent repetition
        S1.ring_setting(), S2.ring_setting(), S3.ring_setting()  ##Applies ring setting
        output = ""
        word = word.replace(" ", "X")
        word = word.replace("?", "QUESTIONMARK")
        word = word.replace("!", "EXCLAMATIONMARK")
        word = word.replace(".", "PERIOD")
        word = ''.join(e for e in word if e.isalnum())

        for l in word:  ##Iterates through the Script for each component of word (In this case letters)
            l = l.upper()  ##All input are changed to uppercase
            pbd = self.plugboard(l,
                                 PB)  ##Input l goes through Plugboard function with arguments l (letter) and PB (Dictionary for Plugboard)

            ##Forward through Scramblers
            S3.state_up()  ##State increased by one
            self.sp3.set(S3.State)
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
            self.sp2.set(S2.State)
            self.sp1.set(S1.State)
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
            output += (self.plugboard(letter_back3, PB))
        self.Output.set(output)

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
    def plugboard(self, l, PB):
        ##If the letter is in the Plugboard(PB) then it changes its value otherwise it keeps it.
        if l in PB:
            pbo = PB[l]
        else:
            pbo = l
        return pbo


app = EnigmaIApp()
app.geometry("1000x250")
app.mainloop()
