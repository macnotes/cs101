import tkinter as tk
global screen

screen = tk.Tk()
screen.geometry("500x500")
screen.title("My Game")
# screen.backgroud("Red")

lable = tk.Label(text="Hi.",
                 font=("Calibri", 43),
                 height=1
                 ).pack(padx=5, pady=15)

lable = tk.Label(text="What is your name?",
                 font=("Calibri", 23),
                 width=20,
                 height=1
                 ).pack()

entry = tk.Entry(fg="blue",
                 bg="lightgrey",
                 width=30).pack()

your_name = StringVar()
e = Entry(master, textvariable=your_name)
e.pack()

v.set("a default value")
s = v.get()

def handle_click(event):
    print("The button was clicked!")


# Label(text="").pack()
# button1 = tk.Button(text="OK",
#                     font=("Calibri", 33),
#                     width=5,
#                     height=1,
#                     foreground="Blue",  # Set the text color to white
#                     background="Yellow"  # Set the background color to black
#                     ).place(x=370, y=430)
# button1.bind("<Button-1>", handle_click)

button = tk.Button(text="Click me!")
button.bind("<Button-1>", handle_click)
button.pack()

# pack(side=tk.BOTTOM, padx=5, pady=15)

# ,

# Label(text="").pack()
# Button(text="answer2").pack()
screen.mainloop()


# from tkinter import ttk
# global screen
# screen = ttk()
# screen.geometry("500x500")
# screen.title("4rManager")
