import functions
from user_interface import display



input_notes = ["C4", "C5"]
instrument = 48
degree = 4

def func():
    roots, comp = functions.create_trie(degree)
    melody = functions.generate(input_notes, 50, roots, degree)
    functions.pitch_to_midi(melody, [400]*len(melody), instrument)

display(func())

