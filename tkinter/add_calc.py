from tkinter import *

root = Tk() # First lines(basic window)
root.title("Simple calc")

entry = Entry(root, width=35, fg="black", borderwidth=5)
entry.grid(row=0, column=0, columnspan=3, padx=10, pady=5)


def button_click(number):
    current = entry.get()
    entry.delete(0, END)
    entry.insert(0, str(current) + str(number))


def button_clear():
    current = ""
    entry.delete(0, END)


def button_add():
    val = entry.get()
    global val_1
    val_1 = int(val)
    current = ""
    entry.delete(0, END)


def button_equal():
    val_2 = entry.get()
    current = ""
    entry.delete(0, END)
    entry.insert(0, val_1 + int(val_2))


button_1 = Button(root, text="1", padx=40, pady=20, command=lambda: button_click(1))
button_2 = Button(root, text="2", padx=40, pady=20, command=lambda: button_click(2))
button_3 = Button(root, text="3", padx=40, pady=20, command=lambda: button_click(3))
button_4 = Button(root, text="4", padx=40, pady=20, command=lambda: button_click(4))
button_5 = Button(root, text="5", padx=40, pady=20, command=lambda: button_click(5))
button_6 = Button(root, text="6", padx=40, pady=20, command=lambda: button_click(6))
button_7 = Button(root, text="7", padx=40, pady=20, command=lambda: button_click(7))
button_8 = Button(root, text="8", padx=40, pady=20, command=lambda: button_click(8))
button_9 = Button(root, text="9", padx=40, pady=20, command=lambda: button_click(9))
button_0 = Button(root, text="0", padx=40, pady=20, command=lambda: button_click(0))
button_add = Button(root, text="+", padx=40, pady=20, command=button_add)
button_clear = Button(root, text="Clear", padx=120, pady=20, command=button_clear)
button_equal = Button(root, text="=", padx=40, pady=20, command=button_equal)


button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)
button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_add.grid(row=4, column=0)
button_0.grid(row=4, column=1)
button_equal.grid(row=4, column=2)

button_clear.grid(row=5, column=0, columnspan=3)

root.mainloop()#event loop
