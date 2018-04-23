from tkinter import *
from tkinter import messagebox
import random

numbers = random.sample(range(0,1000),25)
root = Tk()
root.title("From Lowest to Highest")
ind = 0
errorList = []
errors = StringVar()

def findMin(i,n):
    global ind, errorList

    numbers.sort()
    if int(numbers[ind]) == buttons[i].cget('text'):
        buttons[i].config(state=DISABLED)
        ind=ind+1
    else:
        errorList.append(1)
        errors.set("Errors: " + str(len(errorList)))
    if ind == 25:
        messagebox.showinfo("Congratulation!", "Congratulation! You finished your task.")
    
buttons = []

for i in range(25):
    x = numbers[i]
    x = int(x)
    button = Button(root, text=x, width=12, command=lambda i=i, x=x: findMin(i,x))
    button.grid(row=i%5, column=i//5)
    buttons.append(button)

ErrorCounter = Label(root, text="Errors: 0", textvariable=errors)
ErrorCounter.grid(row=5, column=0)

root.mainloop()
