from tkinter import * 

def sayHelloWorld():
   print("Hello World")

def sayHi():
    print("Hi")

MainWindow = Tk() 
button = Button(MainWindow,text = "Click me1",command = sayHelloWorld).grid(row=0,column=0)
button2 = Button(MainWindow,text = "Click me2",command = sayHi).grid(row=0,column=1)
button3 = Button(MainWindow,text = "Click me3",command = sayHi).grid(row=1,column=1)
MainWindow.mainloop() 