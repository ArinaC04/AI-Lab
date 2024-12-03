from tkinter import *
root = Tk()
w = Label(root, text='Music generation using Markov Chains')
w.pack()


button = Button(root, text='Stop', width=25, command=root.destroy)
button.pack()



root.mainloop()
