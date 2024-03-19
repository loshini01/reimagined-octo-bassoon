import tkinter as tk
from tkinter import messagebox


var = ""
A = 0
operator = ""


def button_is_Clicked(number):
    global var
    var = var + str(number)
    the_data.set(var)


def button_operation_Clicked(op):
    global A, var, operator
    A = float(var)
    operator = op
    var = ""
    the_data.set(var)

def button_equal_Clicked():
    global A, var, operator
    if operator == "+":
        result = A + float(var)
    elif operator == "-":
        result = A - float(var)
    elif operator == "*":
        result = A * float(var)
    elif operator == "/":
        if float(var) == 0:
            messagebox.showerror("Error", "Division by zero!")
            result = "Error"
        else:
            result = A / float(var)
    the_data.set(str(result))
    var = ""

# function for the clear button
def button_clear_Clicked():
    global var, A, operator
    var = ""
    A = 0
    operator = ""
    the_data.set(var)

# GUI window
guiWindow = tk.Tk()
guiWindow.title("Loshi Calculator")
guiWindow.geometry("320x500+400+400")

# label for the window
the_data = tk.StringVar()
guiLabel = tk.Label(
    guiWindow,
    text="",
    anchor=tk.SE,
    font=("Cambria Math", 20),
    textvariable=the_data,
    background="light pink",
    fg="black"
)
guiLabel.grid(row=0, column=0, columnspan=4, sticky="nsew")

# Creating the buttons
buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("+", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("-", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("*", 3, 3),
    ("C", 4, 0), ("0", 4, 1), ("=", 4, 2), ("/", 4, 3)
]

for (text, row, col) in buttons:
    button = tk.Button(
        guiWindow,
        text=text,
        font=("Cambria", 22),
        background="light blue",
        relief=tk.GROOVE,
        border=0,
        command=lambda t=text: button_is_Clicked(t) if t.isdigit() or t == "." else (button_operation_Clicked(t) if t in "+-*/" else (button_equal_Clicked() if t == "=" else button_clear_Clicked()))
    )
    button.grid(row=row, column=col, sticky="nsew")


for i in range(5):
    guiWindow.grid_rowconfigure(i, weight=1)
for i in range(4):
    guiWindow.grid_columnconfigure(i, weight=1)


guiWindow.mainloop()
