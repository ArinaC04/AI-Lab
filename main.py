# user interface demo
# core functionality:
#   midi file to sheet music
#   creating the structure for markov's chain
#   predicting next note based on last note
# convert back to midi file
# output and download

# unit tests
# test coverage
# code quality

import functions
import user_interface

input = ["C#3", "E3"]
instrument = 48
functions.create_trie()
melody = functions.generate(input, 50)
functions.pitch_to_midi(melody, instrument)