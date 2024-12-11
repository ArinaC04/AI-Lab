*This will still be edited*
1. With poetry install the dependencies in the virtual engine (poetry install)
2. Run the main.py file
3. Listen to the generated melody or download it anywhere. FYI, a started melody cannot be stopped (believe me, I tried, but turns out stopping is harder that playing it) 

PS: If it gives an error about ports and doesn't play the music:
1. Install the VirtualMidiSynth file present in the repository
2. Once it is there, open it and add a soundfile (https://github.com/urish/cinto/blob/master/media/FluidR3%20GM.sf2)
3. Now you can close it
Run the following commands in a test file:

import mido

print(mido.get_output_names())

There has to be one named something along the lines VirtualMidiSynth, copy it as a string
Then in the main.py file, go to the play_file function and change the port variable to the copied string. Now run it again
