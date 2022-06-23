from tkinter import * 

def sayHelloWorld():
   print("Hello World")

MainWindow = Tk() 
label = Label(MainWindow, text = "Hello World", width=20, fg = "red", bg = "blue",font=("Sarabum",35),anchor=W).grid(row=0,column=1) # W ชิดซ้าย , E ชิดขวา

MainWindow.mainloop() 