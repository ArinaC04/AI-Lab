import functions
import mido


degree=4
instrument = 48
input = ["C5", "C6"]



roots, comp = functions.create_trie(degree)
melody, duration = functions.generate(input, 500, roots, degree)
functions.pitch_to_midi(melody, [x for x in duration if x!=0], instrument)

midi = mido.MidiFile("output.mid")
port = mido.get_output_names()[0]
with mido.open_output(port) as output:
    for message in midi.play():
        output.send(message)