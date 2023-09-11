from tkinter import *

def addition():
    global butClick, answerDisp, errorText, mode, process

    # Get the values from the entry widgets and convert them to float
    number1 = firstNumEntry1.get()
    number2 = secondNumEntry1.get()
    if butClick % 2 == 0:
        try:
            floatNum1 = float(number1)
            floatNum2 = float(number2)
            answer = floatNum1 + floatNum2
            ansTxt = "Calculation: " + number1 + " + " + number2

            answerDisp = Label(root, text="= " + str(answer))
            answerDisp.grid(row=6, column=0,columnspan=5,sticky="w")

            mode = Label(root,text="Mode: [Add]")
            mode.grid(row=4,column=0,pady=5)

            process = Label(root,text=ansTxt)
            process.grid(row=5,column=0,columnspan=5,sticky="w")
        except ValueError:
            errorText = Label(root, text="Error, try again.")
            errorText.grid(row=6, column=0,columnspan=3)
    else:
        answerDisp.grid_forget()
        errorText.grid_forget()
        mode.grid_forget()
        process.grid_forget()
    butClick += 1

def substraction():
    global butClick, answerDisp, errorText, mode, process

    # Get the values from the entry widgets and convert them to float
    number1 = firstNumEntry1.get()
    number2 = secondNumEntry1.get()
    if butClick % 2 == 0:
        try:
            floatNum1 = float(number1)
            floatNum2 = float(number2)
            answer = floatNum1 - floatNum2
            ansTxt = "Calculation: " + number1 + " - " + number2

            answerDisp = Label(root, text="= " + str(answer))
            answerDisp.grid(row=6, column=0,columnspan=5,sticky="w")

            mode = Label(root,text="Mode: [Sub]")
            mode.grid(row=4,column=0,pady=5)

            process = Label(root,text=ansTxt)
            process.grid(row=5,column=0,columnspan=5,sticky="w")
        except ValueError:
            errorText = Label(root, text="Error, try again.")
            errorText.grid(row=6, column=0,columnspan=3)
    else:
        answerDisp.grid_forget()
        errorText.grid_forget()
        mode.grid_forget()
        process.grid_forget()
    butClick += 1

def multiplication():
    global butClick, answerDisp, errorText,mode, process

    # Get the values from the entry widgets and convert them to float
    number1 = firstNumEntry1.get()
    number2 = secondNumEntry1.get()
    if butClick % 2 == 0:
        try:
            floatNum1 = float(number1)
            floatNum2 = float(number2)
            answer = floatNum1 * floatNum2
            ansTxt = "Calculation: " + number1 + " * " + number2

            answerDisp = Label(root, text="= " + str(answer))
            answerDisp.grid(row=6, column=0,columnspan=5,sticky="w")

            mode = Label(root,text="Mode: [Mul]")
            mode.grid(row=4,column=0,pady=5)
            
            process = Label(root,text=ansTxt)
            process.grid(row=5,column=0,columnspan=5,sticky="w")
        except ValueError:
            errorText = Label(root, text="Error, try again.")
            errorText.grid(row=6, column=0,columnspan=3)
    else:
        answerDisp.grid_forget()
        errorText.grid_forget()
        mode.grid_forget()
        process.grid_forget()
    butClick += 1

def division():
    global butClick, answerDisp, errorText, mode, process

    # Get the values from the entry widgets and convert them to float
    number1 = firstNumEntry1.get()
    number2 = secondNumEntry1.get()
    if butClick % 2 == 0:
        try:
            floatNum1 = float(number1)
            floatNum2 = float(number2)
            answer = floatNum1 / floatNum2
            ansTxt = "Calculation: " + number1 + " / " + number2

            answerDisp = Label(root, text="= " + str(answer))
            answerDisp.grid(row=6, column=0,columnspan=5,sticky="w")

            mode = Label(root,text="Mode: [Div]")
            mode.grid(row=4,column=0,pady=5)

            process = Label(root,text=ansTxt)
            process.grid(row=5,column=0,columnspan=5,sticky="w")
        except ValueError:
            errorText = Label(root, text="Error, try again.")
            errorText.grid(row=6, column=0,columnspan=3)
    else:
        answerDisp.grid_forget()
        errorText.grid_forget()
        mode.grid_forget()
        process.grid_forget()
    butClick += 1

root = Tk()
root.geometry("260x160")
root.title("Compact Calculator")
root.resizable(False, False)
root.iconbitmap("calcGui.ico")

# initialization
butClick = 0
answerDisp = Label(root, text="")
errorText = Label(root, text="")
mode = Label(root, text="")
process = Label(root, text="")

# entry/button data
firstNumTxt1 = Label(root, text="First Number: ").grid(row=1, column=0, sticky="e")
secondNumTxt1 = Label(root, text="Second Number: ", pady=5).grid(row=2, column=0, sticky="e")
opText = Label(root, text="Choose Operation: ").grid(row=3, column=0, sticky="w", rowspan=1)

firstNumEntry1 = Entry(root)
secondNumEntry1 = Entry(root)

addBut = Button(root, text="Add", padx=15, command=addition)
subBut = Button(root, text="Subtract", padx=4, command=substraction)
mulBut = Button(root, text="Multiply", padx=4, command=multiplication)
divBut = Button(root, text="Divide", padx=9, command=division)

# entry/button grid
firstNumEntry1.grid(row=1, column=1, columnspan=2)
secondNumEntry1.grid(row=2, column=1, columnspan=2)

addBut.grid(row=3, column=1, sticky="es")
subBut.grid(row=3, column=2, sticky="ws")
mulBut.grid(row=4, column=1, sticky="en")
divBut.grid(row=4, column=2, sticky="wn")

root.mainloop()