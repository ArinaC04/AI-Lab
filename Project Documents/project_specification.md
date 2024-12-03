# Project spcification: Music generation
## Programming language

1. Python
2. I am also proficient in C++ if needed

## Algorithms and data structures

1. **Markov Chain**: The core of the program is a Markov Chain model that will generate sequences based on the probabilities of note transitions. This includes creating first-order and higher-order Markov Chains to capture both basic and more complex patterns in the music, like rithm and melody.
2. **Transition Matrix**: The transition probabilities are stored in a matrix, where each element represents the probability of moving from one note (or sequence of notes) to another. This will be implemented using trie tree.

## Problem

The goal is to generate musically coherent sequences using probabilistic modeling, capturing melodic and rhythmic patterns from a dataset to generate original pieces.

## Input

The primary input will be a dataset of MIDI files. Each MIDI file provides:
Note Sequences: Used to calculate the probability of transitions between notes.
Rhythmic Values: Used to build a rhythm-based Markov Chain.
**Usage**: The program will analyse these files, convert sequences into transitions and calculate probabilities, which will create a transition matrix for each musical aspect (melody, rhythm). This matrix will be the foundation for the generation of new sequences.

## References

Python Libraries: markovify (for Markov Chains), mido and midiutil (for MIDI processing), music21 (for music analysis).

## Degree

Bachelor's Programme in Science (computer science track)
