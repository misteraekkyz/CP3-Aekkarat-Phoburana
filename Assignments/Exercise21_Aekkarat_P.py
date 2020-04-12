from tkinter import *
import math

def leftClickButton(event):

    squared = math.pow(float(textBoxHeight.get())/100,2)
    cal = float(textBoxWeight.get())/squared
    print(cal)
    labelResult.configure(text = cal)

def leftClickButton2(event):
    squared = math.pow(float(textBoxHeight.get()) / 100, 2)
    cal = float(textBoxWeight.get()) / squared
    if cal > 30.0:
        print(recommentButton.configure(text = 'Very fat'))
    elif cal >= 25.0 and cal <=29.9:
        print(recommentButton.configure(text = 'Fat'))
    elif cal >= 23.0 and cal <= 24.9:
        print(recommentButton.configure(text = 'Over Weight'))
    elif cal >= 18.6 and cal <= 22.9:
        print(recommentButton.configure(text = 'Normal Weight'))
    elif cal < 18.5:
        print(recommentButton.configure(text = 'Thin'))

mainWindow = Tk()

labelHeight = Label(mainWindow,text='Height(cm)',fg= "white" , bg = "green")
labelHeight.grid(row=0,column=0)

textBoxHeight = Entry(mainWindow)
textBoxHeight.grid(row=0,column=1)

labelWeight = Label(mainWindow,text='Weight(kg)',fg= "black" , bg = "yellow")
labelWeight.grid(row=1,column=0)

textBoxWeight = Entry(mainWindow)
textBoxWeight.grid(row=1,column=1)

calculateButton = Button(mainWindow,text='Calculate')
calculateButton.bind('<Button-1>',leftClickButton)
calculateButton.grid(row=2,column=0)

labelResult = Label(mainWindow, text = 'Result ')
labelResult.grid(row=2, column=1)

commentButton = Button(mainWindow,text='Comment')
commentButton.grid(row=3, column=0)

recommentButton = Button(mainWindow,text='Calculate')
recommentButton.bind('<Button-1>',leftClickButton2)
recommentButton.grid(row=3,column=1)

mainWindow.mainloop()