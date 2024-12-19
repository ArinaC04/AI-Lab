# Music Generation with Markov Chains

## Overview

This is a music generation project based on Markov Chains. The user interface takes starting notes, instrument and degree of Markov Chain as input and outputs a melody based on these parameters and probabilistic transitions between notes. The generated melody is available for playback or for download, both from the user interface.

## Features

- Choose the starting notes.
- Define the instrument from General MIDI Instrument Set.
- Edit the degree of the Markov Chain for melody generation.
- Generate melodies.
- Playback and save the generated MIDI files.

## Project Structure

```
AI-Lab
├── MIDI -- folder that contains training data
├── Project Documents
    ├──project_specification.md --initial definition of the project
    ├──implementation_document.md --how was the idea and algorithm implemented
    ├──testing_document.md --how was the project tested and how to run the tests yourself
    ├──user_guide.md --clear instructions for using the project and generating melodies
├──Weekly Reports --folder with the weekly reports
├── functions.py -- contains the helper functions for the core algorithm
├── main.py -- contains the base window of the user interface
├── ui.py -- contains the adjacent functions for the well-being of the user interface
├── C6_C6_C6.mid --example file that was generated to see how the program reacts to the repetition of the same note
├── poetry.lock -- poetry file for installing dependencies
├── poetry.toml -- poetry file for installing dependencies
├── README.md --what you're reading now :)
├── jackson_m.mid --file used for rythm
├── CoolSoft_VirtualMIDISynth_2.13.9.exe --virtual synthetizer for the cases when your device gives and error and doesn't play the generated melody
├── test_midi_to_pitch.py -- test file for the midi_to_pitch function
├── test_note.py -- test file for the note function
├── test_midi.py -- test file for the midi function
└── test_generate.py -- test file for the generation function
```

### `functions.py`
Contains core logic for:
- MIDI note conversion to pitch and vice versa.
- MIDI file handling.
- Creation of the trie
- Generating the melody
  
### `main.py`
The main user interface:
- Input fields for melody generation parameters.
- Buttons for viewing instrument lists and generating melodies.
- Tkinter-based GUI setup.

### `ui.py`
Handles user interactions:
- Error handling for incorrect inputs.
- Melody generation logic.
- Displaying instrument lists and output options.

## Usage

You can find a detailed setup instructions in the user_guide.md file in folder Project Documents
