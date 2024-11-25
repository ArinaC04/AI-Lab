# user interface demo
# core functionality:
#   midi file to sheet music
#   creating the structure for markov's chain
#   predicting next note based on last note
# convert back to midi file
# output and download

# unit tests
# test coverage

import functions
import user_interface 




input_notes = ["C4", "C5"]
instrument = 48
roots = functions.create_trie()
melody = functions.generate(input_notes, 50, roots)
functions.pitch_to_midi(melody, [400]*len(melody), instrument)
