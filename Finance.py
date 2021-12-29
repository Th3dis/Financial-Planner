from tkinter import ttk
from tkinter import *

vals = []

def getNum():
    vals.append(entry.get())

def getNum2():
    vals.append(entry2.get())

def getNum3():
    vals.append(entry3.get())

def getNum4():
    vals.append(entry4.get())

def calc():
    sum = int(vals[0])
    for x in range(1, len(vals)):
        sum -= int(vals[x])
    text = StringVar()
    text.set('You have ' + str(sum) + ' surplus dollar(s)! Don\'t spend it all in one place!')
    print(text)


    finalLabel = Label(root, textvariable=text)
    finalLabel.grid()



root = Tk()
root.title('Finances')
root.geometry("960x1080")

title = Label(root, text='Financial Planner', font=('Calibri', 100), fg='green')
title.grid()


assets = Label(root, text='Monthly post-tax income:', font=('Calibri', 30), fg='green', padx=100)
assets.grid()

entry = Entry(root,width=100)
entry.grid()

confirm = Button(root, text='Confirm', command=getNum)
confirm.grid()

food = Label(root, text='Money spent on groceries:', font=('Calibri', 30), fg='green')
food.grid(row=4,column=0)

entry2= Entry(root,width=100)
entry2.grid()

confirm2 = Button(root,text='Confirm', command=getNum2)
confirm2.grid()

rent = Label(root, text='Money spent on rent/utilities:', font=('Calibri', 30), fg='green')
rent.grid()

entry3=Entry(root,width=100)
entry3.grid()

confirm3=Button(root,text='Confirm',command=getNum3)
confirm3.grid()

savings = Label(root, text='Savings:', font=('Calibri', 30), fg='green')
savings.grid()

entry4=Entry(root,width=100)
entry4.grid()

confirm4=Button(root,text='Confirm', command=getNum4)
confirm4.grid()

calculate = Button(root, text='Calculate', command=calc)
calculate.grid(pady=150)




root.mainloop()
