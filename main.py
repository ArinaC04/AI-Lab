from tkinter import *
import functions
import re


def func(input_notes, instrument, degree):
    input_notes = input_notes.get()
    pitch_pattern = r'[A-G][#]?\d+'
    input = re.findall(pitch_pattern, input_notes)
    instrument = int(instrument.get())
    degree = int(degree.get())
    roots, comp = functions.create_trie(degree)
    melody = functions.generate(input, 50, roots, degree)
    functions.pitch_to_midi(melody, [400]*len(melody), instrument)



root = Tk()
w = Label(root, text='Music generation using Markov Chains').grid(row=0)

Label(root, text='Input notes').grid(row=1)
T1 = Message(root, text = 'Write here the starting notes for the melody. They should range from C1 to C12. Ex: C1, A3')
T1.grid(row=2)
T1.config(bg='lightgreen')

Label(root, text='Instrument').grid(row=3)
T2 = Text(root, height=2, width=30)
T2.grid(row=4)
T2.insert(END, 'What instrument would you like to use?\n ')
T2.config(state=DISABLED)



Label(root, text='Degree of Markov Chain').grid(row=5)
T3 = Text(root, height=2, width=30)
T3.grid(row=6)
T3.insert(END, 'How many notes would you like for the model to take into consideration when generating music?')
T3.config(state=DISABLED)


input = Entry(root)
instrument = Spinbox(root, from_=0, to=127)
degree = Entry(root)


input.grid(row=1, column=1)
instrument.grid(row=3, column=1)
degree.grid(row=5, column=1)


button = Button(root, text='Generate', width=25, command=lambda: func(input, instrument, degree))
button.grid(row = 7)



mainloop()
