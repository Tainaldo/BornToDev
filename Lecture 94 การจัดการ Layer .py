from tkinter import * 

def sayHelloWorld():
   print("Hello World")

def sayHi():
    print("Hi")

MainWindow = Tk() 
button = Button(MainWindow,text = "Click me",command = sayHelloWorld).grid(row=0,column=0)
button2 = Button(MainWindow,text = "Click me",command = sayHi).grid(row=1,column=1)
MainWindow.mainloop() 