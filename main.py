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

from mido import MidiFile, MidiTrack, Message
import random
import os


def note(midi_note):
    notes = [
        'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B'
    ]
    octave = (midi_note // 12) - 2  
    note_name = notes[midi_note % 12]
    return f"{note_name}{octave}"


def midi(note):
    notes = [
        'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B'
    ]
    i=0
    while notes[i]!=note[:-1]:
        i+=1
        
    return (int(note[-1])+2) * 12 + i



def midi_to_pitch(file):
    midi_file = MidiFile(file)
    pitches = []
    duration = []
    midi_pitches = []
    for track in midi_file.tracks:
        for msg in track:
            if msg.type == 'note_on':  # note_on event
                #pitch = midi_to_pitch(msg.note)  # Convert MIDI number to pitch name
                pitches.append(note(msg.note))
                midi_pitches.append(msg.note)
            if msg.type == 'note_off':  # note_on event
                duration.append(msg.time)
            # if msg.type == 'program_change':
            #     print(msg.program)
    return pitches, duration



def pitch_to_midi(pitches, instrument):
    notes = []
    # Create a new MIDI file
    midi_file = MidiFile()
    track = MidiTrack()
    midi_file.tracks.append(track)
    track.append(Message('program_change', program=instrument))
    for i in range(len(pitches)):
        notes.append((midi(pitches[i]), 300))
        #notes.append((midi(pitches[i]), duration[i]))
    for pitch, d in notes:
        track.append(Message('note_on', note=pitch, velocity=64, time=0))  # Start the note
        track.append(Message('note_off', note=pitch, velocity=64, time=d))  # Stop the note after 'duration' ticks

    midi_file.save('output.mid')



class Node:
    def __init__(self, note):
        self.note = note
        self.probability = 0
        self.freq = 1
        self.children = {}
    
    def add_child(self, note):
        self.children[note] = Node(note)

    
    def new_notes(self, note2, note3):
        self.freq += 1
        if note2 in self.children:
            for child in self.children:
                if child == note2:
                    self.children[child].freq += 1
                    if note3 in self.children[child].children:
                        for child2 in self.children[child].children:
                            if child2 == note3:
                                self.children[child].children[child2].freq += 1
                    else:
                        self.children[child].add_child(note3)
        else:
            self.add_child(note2)
            self.children[note2].add_child(note3)



def get_prob():
    for root in roots.values():
        for node2 in root.children:
            root.children[node2].probability = root.children[node2].freq/root.freq
            for node3 in root.children[node2].children:
                root.children[node2].children[node3].probability = root.children[node2].children[node3].freq/root.children[node2].freq


def print_trie():
    for root in roots.values():
        print(root.note)
        for node2 in root.children:
            print("\t", node2, round(root.children[node2].probability, 2))
            for node3 in root.children[node2].children:
                print("\t\t", node3, round(root.children[node2].children[node3].probability, 2))

        print("\n \n")

#pitches = ["C", "A", "D", "C", "B", "A", "C", "A", "E", "C", "B", "E", "C", "B", "A"]
roots = {}
def trie(pitches, duration):
    for i in range(len(pitches)-2):
        if pitches[i] not in roots:
            roots[pitches[i]] = Node(pitches[i])
            roots[pitches[i]].freq -= 1
        roots[pitches[i]].new_notes(pitches[i+1], pitches[i+2])
    get_prob()

directory = 'MIDI'
files = os.listdir(directory)
for file in files:
    pitches, duration = midi_to_pitch("MIDI/"+file)
    trie(pitches, duration)

print_trie()

input = ["C#3", "E3"]
melody = input.copy()

for i in range(50):
    note1 = melody[i]
    note2 = melody[i+1]
    node2 = roots[note1].children[note2]
    dist = list(node2.children.keys())
    weights = list([j.probability*100 for j in node2.children.values()])
    pred_note = random.choices(dist, weights = weights, k = 1)[0]
    melody.append(pred_note)
    #print(pred_note)
print(melody)


instrument = 48
pitch_to_midi(melody, instrument)