#!/usr/local/bin/python3

def main_screen():
  from tkinter import ttk

  global screen
  screen = tk()

  screen.geometry("500x500")
  screen.title("My Game")

  Label(text="Hi.", font=("Calibri", 13)).pack()
  ttk.Label(text="").pack()
  ttk.Button(text="answer1").pack()
  ttk.Label(text="").pack()
  ttk.Button(text="answer2").pack()

  screen.mainloop()

main_screen()
print("Done.")
