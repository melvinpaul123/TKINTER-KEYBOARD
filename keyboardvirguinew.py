from tkinter import *
import tkinter as tk

kb = tk.Tk()

buttons = [
'ESC', '~', '`', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', 'ENTER',
'TAB', 'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', '\\', '/', '1', '2', '3','BACKSPACE',
'.com', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', '[', ']', '=', '4', '5', '6', 'SPACE',
'SHIFT','z', 'x', 'c', 'v', 'b', 'n', 'm', ',', '.', '?', '{', '}', '7', '8', '9', '0',
]

def select(value):
    if value == "ESC":
        entry.delete(1.0,tk.END)
    elif value == "SPACE":
        entry.insert(tk.END, ' ')
    elif value == "BACKSPACE":
        if len(entry.get(1.0,tk.END))<=1:
            new=""
        else:
            new = entry.get(1.0,tk.END)[:-2]
        entry.delete(1.0,tk.END)
        entry.insert(tk.END, new)
    elif value == "TAB":
        entry.insert(tk.END, '    ')
    elif value == "ENTER":
        entry.insert(tk.END, '\n')
    else :
        entry.insert(tk.END,value)

def HosoPop():

	varRow = 3
	varColumn = 0

	for button in buttons:

		command = lambda x=button: select(x)
		
		if button == "SPACE" or button == "SHIFT" or button == "BACKSPACE" or button == "ENTER" or button == "ESC" or button == ".com" or button == "0" or button == "TAB":
			tk.Button(kb,text= button,width=16, height=2, bg="#000000", fg="#ffffff",
				activebackground = "#ffffff", activeforeground="#000000", relief='raised', padx=1,
				pady=1, bd=1,command=command).grid(row=varRow,column=varColumn)

		else:
			tk.Button(kb,text= button,width=8,height=2, bg="#000000", fg="#ffffff",
				activebackground = "#ffffff", activeforeground="#000000", relief='raised', padx=1,
				pady=1, bd=1,command=command).grid(row=varRow,column=varColumn)


		varColumn +=1 

		if varColumn > 16 and varRow == 3:
			varColumn = 0
			varRow+=1
		if varColumn > 16 and varRow == 4:
			varColumn = 0
			varRow+=1
		if varColumn > 16 and varRow == 5:
			varColumn = 0
			varRow+=1



kb.title("VIRTUAL KEYBOARD GUI")
kb.resizable(0,0)
	

label1 = tk.Label(kb,text='      VIRTUAL KEYBOARD         ').grid(row=0,columnspan=17)

entry =tk.Text(kb, width=106,height=10,font=("arial",15,"bold"),wrap=tk.WORD)
entry.grid(row=1,columnspan=17)
label2 = tk.Label(kb,text='               ').grid(row=2,columnspan=17)
# entry.pack()
HosoPop()

kb.mainloop()