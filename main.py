import functions
import mido
import re
from tkinter import Toplevel, messagebox, filedialog, Message, Label, Entry, Spinbox, Button, Tk, font, Scrollbar, END, LEFT, RIGHT, BOTH, Listbox, Y
import os


def func(input_notes, instrument, degree):
    input_notes = input_notes.get()
    instrument = instrument.get()
    degree = degree.get()
    pitch_pattern = r'[A-G][#]?\d+'
    input = re.findall(pitch_pattern, input_notes)
    if input_notes == "" or input == "" or instrument == "" or degree =="":
        top = Toplevel()
        top.title('Error')
        t = Message(top, text = 'Wrong input. Try again')
        t.grid(row=0)
        t.config(bg='red')
        top.mainloop()
        return
    instrument = int(instrument)
    if instrument < 0 or instrument > 127:
        top = Toplevel()
        top.title('Error')
        t = Message(top, text = 'Wrong instrument. Try again')
        t.grid(row=0)
        t.config(bg='red')
        top.mainloop()
        return
    degree = int(degree)
    roots, comp = functions.create_trie(degree)
    melody = functions.generate(input, 50, roots, degree)
    functions.pitch_to_midi(melody, [400]*len(melody), instrument)
    show_popup()

def inst_list():
        
    GM_INSTRUMENTS = [
        "1. Acoustic Grand Piano", "2. Bright Acoustic Piano", "3. Electric Grand Piano", "4. Honky-Tonk Piano",
        "5. Electric Piano 1", "6. Electric Piano 2", "7. Harpsichord", "8. Clavinet",
        "9. Celesta", "10. Glockenspiel", "11. Music Box", "12. Vibraphone", "13. Marimba", "14. Xylophone",
        "15. Tubular Bells", "16. Dulcimer",
        "17. Drawbar Organ", "18. Percussive Organ", "19. Rock Organ", "20. Church Organ", "21. Reed Organ",
        "22. Accordion", "23. Harmonica", "24. Tango Accordion",
        "25. Acoustic Guitar (nylon)", "26. Acoustic Guitar (steel)", "27. Electric Guitar (jazz)", 
        "28. Electric Guitar (clean)", "29. Electric Guitar (muted)", "30. Overdriven Guitar", 
        "31. Distortion Guitar", "32. Guitar Harmonics",
        "33. Acoustic Bass", "34. Electric Bass (finger)", "35. Electric Bass (pick)", "36. Fretless Bass",
        "37. Slap Bass 1", "38. Slap Bass 2", "39. Synth Bass 1", "40. Synth Bass 2",
        "41. Violin", "42. Viola", "43. Cello", "44. Contrabass", "45. Tremolo Strings", "46. Pizzicato Strings",
        "47. Orchestral Harp", "48. Timpani",
        "49. String Ensemble 1", "50. String Ensemble 2", "51. Synth Strings 1", "52. Synth Strings 2",
        "53. Choir Aahs", "54. Voice Oohs", "55. Synth Voice", "56. Orchestra Hit",
        "57. Trumpet", "58. Trombone", "59. Tuba", "60. Muted Trumpet", "61. French Horn", "62. Brass Section",
        "63. Synth Brass 1", "64. Synth Brass 2",
        "65. Soprano Sax", "66. Alto Sax", "67. Tenor Sax", "68. Baritone Sax", "69. Oboe", "70. English Horn",
        "71. Bassoon", "72. Clarinet",
        "73. Piccolo", "74. Flute", "75. Recorder", "76. Pan Flute", "77. Blown Bottle", "78. Shakuhachi",
        "79. Whistle", "80. Ocarina",
        "81. Lead 1 (square)", "82. Lead 2 (sawtooth)", "83. Lead 3 (calliope)", "84. Lead 4 (chiff)",
        "85. Lead 5 (charang)", "86. Lead 6 (voice)", "87. Lead 7 (fifths)", "88. Lead 8 (bass + lead)",
        "89. Pad 1 (new age)", "90. Pad 2 (warm)", "91. Pad 3 (polysynth)", "92. Pad 4 (choir)",
        "93. Pad 5 (bowed)", "94. Pad 6 (metallic)", "95. Pad 7 (halo)", "96. Pad 8 (sweep)",
        "97. FX 1 (rain)", "98. FX 2 (soundtrack)", "99. FX 3 (crystal)", "100. FX 4 (atmosphere)",
        "101. FX 5 (brightness)", "102. FX 6 (goblins)", "103. FX 7 (echoes)", "104. FX 8 (sci-fi)",
        "105. Sitar", "106. Banjo", "107. Shamisen", "108. Koto", "109. Kalimba", "110. Bagpipe", 
        "111. Fiddle", "112. Shanai",
        "113. Tinkle Bell", "114. Agogo", "115. Steel Drums", "116. Woodblock", "117. Taiko Drum", 
        "118. Melodic Tom", "119. Synth Drum", "120. Reverse Cymbal",
        "121. Guitar Fret Noise", "122. Breath Noise", "123. Seashore", "124. Bird Tweet", 
        "125. Telephone Ring", "126. Helicopter", "127. Applause", "128. Gunshot"
    ]
    popup = Toplevel()
    popup.title("General MIDI Instruments")
    popup.geometry("400x500")
    
    scrollbar = Scrollbar(popup)
    scrollbar.pack(side=RIGHT, fill=Y)
    
    listbox = Listbox(popup, yscrollcommand=scrollbar.set, width=50, height=25)
    for instrument in GM_INSTRUMENTS:
        listbox.insert(END, instrument)
    listbox.pack(side=LEFT, fill=BOTH)
    
    scrollbar.config(command=listbox.yview)

    close_button = Button(popup, text="Close", command=popup.destroy)
    close_button.pack(pady=10)

def play_file(): 
    midi = mido.MidiFile("output.mid")
    port = mido.get_output_names()[0]
    with mido.open_output(port) as output:
        for message in midi.play():
            output.send(message)

def download_file():
    save_path = filedialog.asksaveasfilename(
        defaultextension=".midi",
        filetypes=[("MIDI files", "*.mid"), ("All files", "*.*")]
    )
    if save_path:
        try:
            os.rename("output.mid", save_path)
            messagebox.showinfo("Success", f"File saved as {save_path}")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save file: {e}")

def show_popup():
    popup = Toplevel()
    popup.title("Output Options")
    popup.geometry("300x200")
    
    Label(popup, text="What would you like to do?").pack(pady=10)
    

    play_button = Button(popup, text="Play", command=lambda: play_file())
    play_button.pack(pady=5)
    
    
    download_button = Button(popup, text="Download", command=lambda: download_file())
    download_button.pack(pady=5)
    
    close_button = Button(popup, text="Close", command=popup.destroy)
    close_button.pack(pady=5)
    
    popup.transient(root)  
    popup.grab_set()       
    root.wait_window(popup) 


root = Tk()
root.title("Music Generation with Markov Chains")
root.geometry("500x400")
root.configure(bg="lightblue")

header_font = font.Font(family="Helvetica", size=16, weight="bold")
label_font = font.Font(family="Arial", size=12)

Label(
    root, text="Music Generation using Markov Chains", font=header_font, bg="lightblue"
).grid(row=0, column=0, columnspan=2, pady=(10, 20))

T1 = Message(
    root,
    text="Write here the starting notes for the melody. They should range from C1 to C12. Ex: C5, C6",
    bg="lightgreen",
    width=400,
    font=label_font,
)
T1.grid(row=2, column=0, columnspan=2, sticky="WE", padx=10, pady=5)

T2 = Message(
    root,
    text="What instrument would you like to use?\nRecommended: 48",
    bg="lightgreen",
    width=400,
    font=label_font,
)
T2.grid(row=4, column=0, columnspan=2, sticky="WE", padx=10, pady=5)

T3 = Message(
    root,
    text="How many notes would you like for the model to take into consideration when generating music? Max 40",
    bg="lightgreen",
    width=400,
    font=label_font,
)
T3.grid(row=6, column=0, columnspan=2, sticky="WE", padx=10, pady=5)

Label(root, text="Input notes", font=label_font, bg="lightblue").grid(
    row=1, column=0, padx=10, pady=5, sticky="E"
)
input_field = Entry(root, width=30)
input_field.grid(row=1, column=1, padx=10, pady=5, sticky="W")

Label(root, text="Instrument", font=label_font, bg="lightblue").grid(
    row=3, column=0, padx=10, pady=5, sticky="E"
)
instrument_field = Entry(root, width=30)
instrument_field.grid(row=3, column=1, padx=10, pady=5, sticky="W")

Label(root, text="Degree of Markov Chain", font=label_font, bg="lightblue").grid(
    row=5, column=0, padx=10, pady=5, sticky="E"
)
degree_field = Spinbox(root, from_=0, to=40, width=28)
degree_field.grid(row=5, column=1, padx=10, pady=5, sticky="W")

# Buttons
inst_button = Button(
    root,
    text="View Instruments",
    command=inst_list,
    bg="lightgray",
    font=label_font,
    relief="raised",
)
inst_button.grid(row=8, column=0, padx=10, pady=(10, 20), sticky="E")

generate_button = Button(
    root,
    text="Generate",
    command=lambda: func(input_field, instrument_field, degree_field),
    bg="green",
    fg="white",
    font=label_font,
    relief="raised",
)
generate_button.grid(row=8, column=1, padx=10, pady=(10, 20), sticky="W")

root.mainloop()
