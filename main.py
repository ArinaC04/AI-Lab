from tkinter import *
import functions
import re


def func(input_notes, instrument, degree):
    input_notes = input_notes.get()
    instrument = instrument.get()
    degree = degree.get()
    if input_notes == "" or instrument == "" or degree =="":
        top = Toplevel()
        top.title('Error')
        t = Message(top, text = 'Wrong input. Try again')
        t.grid(row=0)
        t.config(bg='red')
        top.mainloop()
        return
    pitch_pattern = r'[A-G][#]?\d+'
    input = re.findall(pitch_pattern, input_notes)
    instrument = int(instrument)
    degree = int(degree)
    roots, comp = functions.create_trie(degree)
    melody = functions.generate(input, 50, roots, degree)
    functions.pitch_to_midi(melody, [400]*len(melody), instrument)



root = Tk()
w = Label(root, text='Music generation using Markov Chains').grid(row=0)

T1 = Message(root, text = 'Write here the starting notes for the melody. They should range from C1 to C12. Ex: C5, C6')
T1.grid(row=2, columnspan=2, sticky="WE")
T1.config(bg='lightgreen')

T2 = Message(root, text = 'What instrument would you like to use?\n Recommended: 48')
T2.grid(row=4, columnspan=2, sticky="WE")
T2.config(bg='lightgreen')

T3 = Message(root, text = 'How many notes would you like for the model to take into consideration when generating music? Max 40')
T3.grid(row=6, columnspan=2, sticky="WE")
T3.config(bg='lightgreen')

Label(root, text='Input notes').grid(row=1)
Label(root, text='Instrument').grid(row=3)
Label(root, text='Degree of Markov Chain').grid(row=5)


input = Entry(root)
instrument = Entry(root)
degree = Spinbox(root, from_=0, to=40)


input.grid(row=1, column=1)
instrument.grid(row=3, column=1)
degree.grid(row=5, column=1)


button = Button(root, text='Generate', width=25, command=lambda: func(input, instrument, degree))
button.grid(row = 7, columnspan=2, sticky="WE")




mainloop()
