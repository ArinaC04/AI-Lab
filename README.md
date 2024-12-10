*This will still be edited*
1. With poetry install the dependencies in the virtual engine
2. Install the VirtualMidiSynth file present in the repositoryx
3. Once it is there, open it and add a soundfile (https://github.com/urish/cinto/blob/master/media/FluidR3%20GM.sf2)
4. Now you can close it
5. Run the main.py file
6. Listen to the generated melody or download it anywhere. FYI, a started melody cannot be stopped (believe me, I tried, but turns out that stopping it is harder that playing it) 

PS: If it gives an error about ports and doesn't play the music, run the following commands in a test file:
import mido
print(mido.get_output_names())

There has to be one named something along the lines VirtualMidiSynth, copy it as a string
Then in the main.py file, go to the play_file function and change the port variable to the copied string. Now run it again