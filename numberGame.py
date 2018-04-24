from tkinter import *
from tkinter import messagebox
import random

root = Tk()
root.title("From Lowest to Highest")

numbers = random.sample(range(0,1000),25)
ind = 0
errorList = []
errors = StringVar()
count = True
time = StringVar()
s = 0
m = 0


def findMin(i,n):
    global ind, errorList, count

    numbers.sort()
    if int(numbers[ind]) == buttons[i].cget('text'):
        buttons[i].config(state=DISABLED)
        ind=ind+1
    else:
        errorList.append(1)
        errors.set("Errors: " + str(len(errorList)))
    if ind == 25:
        count = False
        messagebox.showinfo("Congratulation!", "Congratulation! You finished your task.")


def timeIt(*args):
    global s, m, count, time
    if s < 10:
        seconds = "0"+str(s)
    else:
        seconds = str(s)
    if s > 59:
        m += 1
        s = 0
        seconds = "0"+str(s)
    if m < 10:
        minutes = "0"+str(m)
    else:
        minutes = str(m)

    time.set(str(minutes) + ":" + str(seconds))
    if count == True:
        root.after(1000, timeIt)
        s += 1
        
    
buttons = []

for i in range(25):
    x = numbers[i]
    x = int(x)
    button = Button(root, text=x, width=12, command=lambda i=i, x=x: findMin(i,x))
    button.grid(row=i%5, column=i//5)
    buttons.append(button)

ErrorCounter = Label(root, textvariable=errors)
ErrorCounter.grid(row=5, column=2)
timer = Label(root, textvariable=time)
timer.grid(row=5, column=0)

timeIt()

root.mainloop()
