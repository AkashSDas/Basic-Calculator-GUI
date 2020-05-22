# ****** Basic Calculator ******

# *******************************

from tkinter import *
from tkinter import messagebox

# ****** Configuring Window ******
root = Tk()
root.geometry('450x550')
root.title('Basic Calculator')
root.resizable(width=False, height=False)

# ****** Heading ******
heading_label = Label(root, text='Basic Calculator', fg='orange', font=('Courier', 28, 'bold'))
heading_label.grid(row=0, column=0, ipadx=10, ipady=10, columnspan=3)

# ****** Entry Field ******
input_field = Entry(root, width=38, fg='purple', font=('Courier', 18, 'italic'), relief=RAISED)
input_field.grid(row=1, column=0, ipadx=10, ipady=10, pady=(0, 10), columnspan=3)

# ****** Functionality of buttons ******

# *** To get which number is clicked ***
def number_button_click(number):
    current_number = input_field.get()
    input_field.delete(0, 'end')
    input_field.insert(0, f"{current_number}{number}")

# *** Clearing the input field ***
def clear():
    input_field.delete(0, 'end')

# *** Addition ***
def addition():
    global math_operation
    global first_number
    try:
        first_number = float(input_field.get())
    except ValueError:
        messagebox.askretrycancel('Invalid Input', 'Try Again')
        return clear()
    math_operation = 'addition'
    input_field.delete(0, 'end')

# *** Subtraction ***
def subtraction():
    global math_operation
    global first_number
    try:
        first_number = float(input_field.get())
    except ValueError:
        messagebox.askretrycancel('Invalid Input', 'Try Again')
        return clear()
    math_operation = 'subtraction'
    input_field.delete(0, 'end')

# *** Multiplication ***
def multiplication():
    global math_operation
    global first_number
    try:
        first_number = float(input_field.get())
    except ValueError:
        messagebox.askretrycancel('Invalid Input', 'Try Again')
        return clear()
    math_operation = 'multiplication'
    input_field.delete(0, 'end')

# *** Division ***
def division():
    global math_operation
    global first_number
    try:
        first_number = float(input_field.get())
    except ValueError:
        messagebox.askretrycancel('Invalid Input', 'Try Again')
        return clear()
    math_operation = 'division'
    input_field.delete(0, 'end')

# *** Performing mathematical operation ***
def equal():
    second_number = float(input_field.get())
    input_field.delete(0, 'end')
    if math_operation == 'addition':
        result = first_number + second_number
        text = f"Operation Performed \n {first_number} + {second_number} = {float(result)}"
        label = Label(root, text=text, font=("Courier", 18, "bold"), anchor=CENTER, relief=SUNKEN)
        label.grid(row=8, column=0, pady=10, ipadx=50, ipady=10, columnspan=3)
    if math_operation == 'subtraction':
        result = first_number - second_number
        text = f"Operation Performed \n {first_number} - {second_number} = {float(result)}"
        label = Label(root, text=text, font=("Courier", 18, "bold"), anchor=CENTER, relief=SUNKEN)
        label.grid(row=8, column=0, pady=10, ipadx=50, ipady=10, columnspan=3)
    if math_operation == 'multiplication':
        result = first_number * second_number
        text = f"Operation Performed \n {first_number} * {second_number} = {float(result)}"
        label = Label(root, text=text, font=("Courier", 18, "bold"), anchor=CENTER, relief=SUNKEN)
        label.grid(row=8, column=0, pady=10, ipadx=50, ipady=10, columnspan=3)
    if math_operation == 'division':
        result = first_number / second_number
        text = f"Operation Performed \n {first_number} / {second_number} = {float(result)}"
        label = Label(root, text=text, font=("Courier", 18, "bold"), anchor=CENTER, relief=SUNKEN)
        label.grid(row=8, column=0, pady=10, ipadx=50, ipady=10, columnspan=3)

    input_field.insert(0, result)

# *** Operators ***
def operation(operator):
    if operator == '+':
        addition()
    if operator == '-':
        subtraction()
    if operator == '*':
        multiplication()
    if operator == '/':
        division()

# ****** Creating and Displaying Buttons ******

texts = ['9', '8', '7', '6', '5', '4', '3', '2', '1', '0']
rows = [2, 2, 2, 3, 3, 3, 4, 4, 4, 5]
columns = [0, 1, 2, 0, 1, 2, 0, 1, 2, 1]
for text, row, column in zip(texts, rows, columns):
    number_btn = Button(root, text=text, padx=66, pady=18, fg='purple', font=("Courier", 18, "bold"), relief=RAISED)
    number_btn.configure(command=lambda number=text: number_button_click(number))
    number_btn.grid(row=row, column=column)

equal_button = Button(root, text='=', command=equal, padx=66, pady=18, fg='green', font=("Courier", 18, "bold"), relief=RAISED)
equal_button.grid(row=5, column=0)

clear_button = Button(root, text='Clear', command=clear, padx=44, pady=18, font=("Courier", 18, "bold"), relief=RAISED)
clear_button.grid(row=5, column=2)

quit_button = Button(root, text='Quit',command=quit, padx=125, pady=18, fg='red', font=("Courier", 18, "bold"), relief=RAISED)
quit_button.grid(row=7, column=1, columnspan=2)

operators = ['+', '-', '*', '/']
for positon, operator in enumerate(operators):
    button = Button(root, text=operator, padx=66, pady=18, fg='green', font=("Courier", 18, "bold"), relief=RAISED)
    button.configure(command=lambda operator=operator: operation(operator))
    if operator == '/':
        positon = 0
        button.grid(row=7, column=positon)
    else:
        button.grid(row=6, column=positon)

# *******************
root.mainloop()

# *******************************
