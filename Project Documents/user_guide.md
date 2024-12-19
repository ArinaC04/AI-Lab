# Melody Generator User Guide

## Getting Started

1. **Clone the Repository**  
   Clone the repository to your local device using Git.

2. **Install Dependencies**  
   Use Poetry to install the required dependencies in a virtual environment:  
   ```bash
   poetry install
   ```

3. **Run the Program**  
   Execute the main script:  
   ```bash
   poetry run main.py
   ```

4. **Listen or Download**  
   - Enjoy the generated melody or download it to your device.  
   - **Note:** Once a melody starts playing, it cannot be stopped. (Trust me, I tried—but stopping it turned out to be harder than playing it!)


---

## Testing

To run the tests included, follow these steps:

1. **Unit Tests**  
   ```bash
   poetry run python -m coverage run -m unittest
   ```

2. **Test coverage**  
   ```bash
   poetry run python -m coverage report -m
   ```
---

## Troubleshooting

### Issue: Error About Ports and No Music Playback

1. **Install VirtualMidiSynth**  
   - Locate the `VirtualMidiSynth` file in the repository and install it.  

2. **Add a Sound File**  
   - Open VirtualMidiSynth and add a sound file. You can use the following file:  
     [FluidR3 GM.sf2](https://github.com/urish/cinto/blob/master/media/FluidR3%20GM.sf2)  

3. **Close VirtualMidiSynth**  
   Once the sound file is added, you can close VirtualMidiSynth.

4. **Check MIDI Ports**  
   Run the following commands in a test file to list available MIDI output ports:  
   ```python
   import mido

   print(mido.get_output_names())
   ```
   Look for an output name similar to `VirtualMidiSynth` and copy it as a string.

5. **Update `main.py`**  
   In the `main.py` file, locate the `play_file` function. Update the `port` variable with the copied string.

6. **Rerun the Program**  
   Save the changes and run the program again:  
   ```bash
   poetry run main.py
   

