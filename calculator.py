from tkinter import *
from tkinter import ttk

operation = ''
temp_number = 0
record = ''

def button_pressed(value):
    global record
    if value == 'C':
        number_entry.delete(0, 'end')
        print(value, "pressed")
    else:
        number_entry.insert("end", value)
        record += str(value)
        block = Label(root, textvariable=record, width=20)
        block.grid(row=6, columnspan=3)
        print(value, "pressed")

def math_button_pressed(value):
    global operation
    global temp_number
    global record
    if number_entry.get() != '':
        operation = value
        temp_number = int(number_entry.get())
        number_entry.delete(0, 'end')
        record += str(temp_number) + operation
        print(temp_number, operation)

def equal_button_pressed():
    global operation
    global temp_number
    global record
    if operation != '' and number_entry.get() != '':
        number = int(number_entry.get())
        if operation == '+':
            solution = temp_number+number
        elif operation == '-':
            solution = temp_number-number
        elif operation == '*':
            solution = temp_number*number
        elif operation == '/':
            solution = temp_number/number
    number_entry.delete(0, 'end')
    number_entry.insert(0, solution)
    record = temp_number, operation, number, '=', solution
    print(record)
    print(temp_number, operation, number, '=', solution)
    operation = ''
    temp_number = 0

root = Tk()
root.title("Calculator")
root.geometry("350x200")
root.resizable("False", "False")

entry_value = StringVar(root, value='')

number_entry = ttk.Entry(root, textvariable=entry_value, width=20)
number_entry.grid(row=0, columnspan=3)

button_reverse = ttk.Button(root, text="1/x", command = lambda:math_button_pressed('1/x'))
button_reverse.grid(row=1, column=0)
button_clear = ttk.Button(root, text="C", command = lambda:button_pressed('C'))
button_clear.grid(row=1, column=1)
button_backspace = ttk.Button(root, text="backspace", command = lambda:button_pressed('backspace'))
button_backspace.grid(row=1, column=2)
button_div = ttk.Button(root, text="/", command = lambda:math_button_pressed('/'))
button_div.grid(row=1, column=3)

button7 = ttk.Button(root, text="7", command = lambda:button_pressed('7'))
button7.grid(row=2, column=0)
button8 = ttk.Button(root, text="8", command = lambda:button_pressed('8'))
button8.grid(row=2, column=1)
button9 = ttk.Button(root, text="9", command = lambda:button_pressed('9'))
button9.grid(row=2, column=2)
button_mult = ttk.Button(root, text='x', command= lambda:math_button_pressed('*'))
button_mult.grid(row=2, column=3)

button4 = ttk.Button(root, text="4", command = lambda:button_pressed('4'))
button4.grid(row=3, column=0)
button5 = ttk.Button(root, text="5", command = lambda:button_pressed('5'))
button5.grid(row=3, column=1)
button6 = ttk.Button(root, text="6", command = lambda:button_pressed('6'))
button6.grid(row=3, column=2)
button_sub = ttk.Button(root, text='-', command = lambda:math_button_pressed('-'))
button_sub.grid(row=3, column=3)

button1 = ttk.Button(root, text="1", command = lambda:button_pressed('1'))
button1.grid(row=4, column=0)
button2 = ttk.Button(root, text="2", command = lambda:button_pressed('2'))
button2.grid(row=4, column=1)
button3 = ttk.Button(root, text="3", command = lambda:button_pressed('3'))
button3.grid(row=4, column=2)
button_sum = ttk.Button(root, text="+", command = lambda:math_button_pressed('+'))
button_sum.grid(row=4, column=3)

button_switchsign = ttk.Button(root, text="+-", command = lambda:math_button_pressed('+-'))
button_switchsign.grid(row=5, column=0)
button0 = ttk.Button(root, text="0", command = lambda:math_button_pressed('0'))
button0.grid(row=5, column=1)
button_comma = ttk.Button(root, text=".", command = lambda:math_button_pressed('.'))
button_comma.grid(row=5, column=2)
button_equal = ttk.Button(root, text="=", command = lambda:equal_button_pressed())
button_equal.grid(row=5, column=3)

root.mainloop()