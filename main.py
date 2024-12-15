from tkinter import Message, Label, Entry, Spinbox, Button, Tk, font
import ui

#base window
root = Tk()
root.title("Music Generation with Markov Chains")
root.geometry("500x400")
root.configure(bg="lightblue")

header_font = font.Font(family="Helvetica", size=16, weight="bold")
label_font = font.Font(family="Arial", size=12)

#input fields
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
    text="How many notes would you like for the model to take into consideration when generating music? The melody is really nice with degree 5",
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
    command=ui.inst_list,
    bg="lightgray",
    font=label_font,
    relief="raised",
)
inst_button.grid(row=8, column=0, padx=10, pady=(10, 20), sticky="E")

generate_button = Button(
    root,
    text="Generate",
    command=lambda: ui.func(input_field, instrument_field, degree_field, root),
    bg="green",
    fg="white",
    font=label_font,
    relief="raised",
)
generate_button.grid(row=8, column=1, padx=10, pady=(10, 20), sticky="W")

root.mainloop()
