import random
import os
from mido import MidiFile, MidiTrack, Message


def note(midi_note):
    if midi_note<128 and midi_note>0:
        notes = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
        octave = (midi_note // 12) - 2  
        note_name = notes[midi_note % 12] 
        return f"{note_name}{octave}"
    else:
        raise ValueError("Invalid MIDI number")
    


def midi(note):
    notes = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
    if isinstance(note, str):
        i=0
        if (len(note) == 2 or (len(note) == 3 and note[1] == '#')) and note[:-1] in notes:
            while notes[i]!=note[:-1]:
                i+=1
            return (int(note[-1])+2) * 12 + i
        elif len(note) in [3, 4] and note[:-2] in notes and note[2:] in ['10', '11', '#10', '#11']:
            while notes[i]!=note[:-2]:
                i+=1
            return (int(note[-2:])+2) * 12 + i
        else:
            raise ValueError("Invalid note")
    else:
        raise ValueError("Invalid note")
        


def midi_to_pitch(file):
    midi_file = MidiFile(file)
    pitches = []
    duration = []
    midi_pitches = []
    for track in midi_file.tracks:
        for msg in track:
            if msg.type == 'note_on':
                pitches.append(note(msg.note))
                midi_pitches.append(msg.note)
            if msg.type == 'note_off':
                duration.append(msg.time)
    return pitches, duration

def pitch_to_midi(pitches, instrument):
    notes = []
    midi_file = MidiFile()
    track = MidiTrack()
    midi_file.tracks.append(track)
    track.append(Message('program_change', program=instrument))
    for i in range(len(pitches)):
        notes.append((midi(pitches[i]), 300))
    for pitch, d in notes:
        track.append(Message('note_on', note=pitch, velocity=64, time=0)) 
        track.append(Message('note_off', note=pitch, velocity=64, time=d))  

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


def get_prob(roots):
    for root in roots.values():
        for node2 in root.children:
            root.children[node2].probability = root.children[node2].freq/root.freq
            for node3 in root.children[node2].children:
                root.children[node2].children[node3].probability = root.children[node2].children[node3].freq/root.children[node2].freq


def print_trie(roots):
    for root in roots.values():
        print(root.note)
        for node2 in root.children:
            print("\t", node2, round(root.children[node2].probability, 2))
            for node3 in root.children[node2].children:
                print("\t\t", node3, round(root.children[node2].children[node3].probability, 2))
        print("\n \n")    


def create_trie():
    directory = 'MIDI'
    files = os.listdir(directory)
    roots = {}
    for file in files:
        pitches, duration = midi_to_pitch("MIDI/"+file)
        for i in range(len(pitches)-2):
            if pitches[i] not in roots:
                roots[pitches[i]] = Node(pitches[i])
                roots[pitches[i]].freq -= 1
            roots[pitches[i]].new_notes(pitches[i+1], pitches[i+2])
        get_prob(roots)
    return roots


def generate(input, n, roots):
    melody = input.copy()
    for i in range(n):
        note1 = melody[i]
        note2 = melody[i+1]
        node2 = roots[note1].children[note2]
        dist = list(node2.children.keys())
        weights = list([j.probability*100 for j in node2.children.values()])
        pred_note = random.choices(dist, weights = weights, k = 1)[0]
        melody.append(pred_note)
    return melody

