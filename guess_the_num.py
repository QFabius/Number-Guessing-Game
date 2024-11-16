# Libraries
import tkinter as tk    # inbuilt functions for creation of GUI window
import random           # generate random numbers

# Initiate GUI window
win = tk.Tk()                       # Create window named win
win.geometry("750x750")             # Specify size of window
win.title("Number Guessing Game")   # Provide title to window

# Variables
num = random.randint(1, 20)

final_score = tk.IntVar()
guess = tk.IntVar()
hint = tk.StringVar()
score = tk.IntVar()

score.set(5)
final_score.set(score.get())

# Functions
def check():
    # Compare entered number to the randomly generated number
    x = guess.get()
    final_score.set(score.get())
    if score.get() > 0:
        if x > 20 or x < 0:
            hint.set("Lost 1 change!")
            score.set(score.get()-1)
            final_score.set(score.get())

        elif num == x:
            hint.set("You won!")
            score.set(score.get()-1)
            final_score.set(score.get())

        elif num > x:
            hint.set("Too low, guess higher")
            score.set(score.get()-1)
            final_score.set(score.get())

        elif num < x:
            hint.set("Too high, guess lower")
            score.set(score.get()-1)
            final_score.set(score.get())
    else:
        hint.set("Game Over!")

def restart():
    return

# Create labels, entry boxes and button
tk.Entry(win, textvariable=guess, width=3, font=('Ubuntu', 50), relief=tk.GROOVE).place(relx=0.5, rely=0.3, anchor=tk.CENTER)
tk.Entry(win, textvariable=hint, width=50, font=('Courier', 15), relief=tk.GROOVE, bg='orange').place(relx=0.5, rely=0.7, anchor=tk.CENTER)
tk.Entry(win, text=final_score, width=2, font=('Ubuntu', 24), relief=tk.GROOVE).place(relx=0.61, rely=0.85, anchor=tk.CENTER)

tk.Label(win, text='Guess the number ', font=('Courier', 25)).place(relx=0.5, rely=0.09, anchor=tk.CENTER)
tk.Label(win, text='Score out of ', font=('Courier', 25)).place(relx=0.3, rely=0.85, anchor=tk.CENTER)


tk.Button(win, width=8, text='CHECK', font=('Courier', 25), command=check, relief=tk.GROOVE, bg='light blue').place(relx=0.5, rely=0.5, anchor=tk.CENTER)
#tk.Button(win, width=8, text='CHECK', font=('Courier', 25), command=check, relief=tk.GROOVE, bg='light blue').place(relx=0.35, rely=0.5, anchor=tk.CENTER)
#tk.Button(win, width=8, text='RESTART', font=('Courier', 25), command=restart, relief=tk.GROOVE, bg='light blue').place(relx=0.65, rely=0.5, anchor=tk.CENTER)

win.mainloop()
