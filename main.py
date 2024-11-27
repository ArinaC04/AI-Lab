import functions
import user_interface 


#degree of markov - parameter

input_notes = ["C4", "C5"]
instrument = 48
roots = functions.create_trie()

functions.print_trie(roots)

melody = functions.generate(input_notes, 50, roots)
functions.pitch_to_midi(melody, [400]*len(melody), instrument)
