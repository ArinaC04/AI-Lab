import random
import os
from mido import MidiFile, MidiTrack, Message


def note(midi_note):
    if isinstance(midi_note, int) and midi_note<128 and midi_note>0:
        notes = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
        octave = (midi_note // 12) + 1  
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
            return (int(note[-1])-1) * 12 + i
        elif len(note) in [3, 4] and note[:-2] in notes and note[1:] in ['10', '11', '#10', '#11']:
            while notes[i]!=note[:-2]:
                i+=1
            return (int(note[-2:])-1) * 12 + i
        else:
            raise ValueError("Invalid note")
    else:
        raise ValueError("Invalid note")

def midi_to_pitch(file):
    try:
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
    except (OSError, IOError):
        raise ValueError("Not a MIDI file")

def pitch_to_midi(pitches, duration, instrument):
    notes = []
    midi_file = MidiFile()
    track = MidiTrack()
    midi_file.tracks.append(track)
    track.append(Message('program_change', program=instrument))
    for i in range(len(pitches)):
        print(pitches[i])
        notes.append((midi(pitches[i]), duration[i]))
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

    
    def new_notes(self, notes):
        self.freq += 1
        path = self
        for note in notes:
            if note in path.children:
                path.children[note].freq += 1
            else:
                path.add_child(note)
            path = path.children[note]
        
def get_prob_recursive(path, degree, actual_degree):
    if actual_degree == degree:
        return 
    for node in path.children:
        path.children[node].probability = path.children[node].freq/path.freq
        get_prob_recursive(path.children[node], degree, actual_degree + 1)


def get_prob(roots, degree):
    for root in roots.values():
        path = root
        get_prob_recursive(path, degree, 0)

def print_trie_recursive(path, degree, actual_degree):
    if actual_degree == degree:
        return 
    for node in path.children:
        print("\t"*(actual_degree + 1), node, round(path.children[node].probability, 2))
        print_trie_recursive(path.children[node], degree, actual_degree + 1)

def print_trie(roots, degree):
    for root in roots.values():
        print(root.note)
        path = root
        print_trie_recursive(path, degree, 0)
        print("\n \n")   


def create_trie(degree):
    directory = 'MIDI'
    files = os.listdir(directory)
    roots = {}
    comp = list()
    for file in files:
        pitches, duration = midi_to_pitch("MIDI/"+file) 
        for i in range(len(pitches)-degree):
            if pitches[i] not in roots:
                roots[pitches[i]] = Node(pitches[i])
                roots[pitches[i]].freq -= 1
            roots[pitches[i]].new_notes(pitches[i + 1: i + degree + 1])    
            comp.append(pitches[i: i + degree + 1])  
        get_prob(roots, degree)
    return roots, comp


def generate(input, n, roots, degree):
    melody = input.copy()
    l = len(melody)
    while l<degree:
        path = roots[melody[0]]
        for j in range(l-1):
            path = path.children[melody[j+1]]
        dist = list(path.children.keys())
        weights = list([j.probability*100 for j in path.children.values()])
        pred_note = random.choices(dist, weights = weights, k = 1)[0]
        melody.append(pred_note)
        l += 1
    for i in range(n):
        seq = melody[i: i + degree]
        path = roots[seq[0]]
        for j in range(len(seq)-1):
            path = path.children[seq[j+1]]
        dist = list(path.children.keys())
        weights = list([j.probability*100 for j in path.children.values()])
        pred_note = random.choices(dist, weights = weights, k = 1)[0]
        melody.append(pred_note)
    return melody

