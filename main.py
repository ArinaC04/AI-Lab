import functions
import user_interface 


#degree of markov - parameter

input_notes = ["C4", "C5"]
instrument = 48
degree = 4
roots, comp = functions.create_trie(degree)

#functions.print_trie(roots, degree)

melody = functions.generate(input_notes, 50, roots, degree)
functions.pitch_to_midi(melody, [400]*len(melody), instrument)
