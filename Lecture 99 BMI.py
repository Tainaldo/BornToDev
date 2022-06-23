from tkinter import *
import math

def leftClickButton(event):
    print(float(textBoxWeight.get())/math.pow(float(textBoxHight.get())/100,2)) # ดึงข้อมูลจาก Entry ใช้ .get()
    labelResult.configure(text = float(textBoxWeight.get())/math.pow(float(textBoxHight.get())/100,2))
    
MainWindow = Tk()
labelHight = Label(MainWindow,text="ส่วนสูง(cm)")
labelHight.grid(row=0,column=0)
textBoxHight = Entry(MainWindow)
textBoxHight.grid(row=0,column=1)
labelWeight = Label(MainWindow,text="น้ำหนัก(Kg)")
labelWeight.grid(row=1,column=0)
textBoxWeight = Entry(MainWindow)
textBoxWeight.grid(row=1,column=1)
calculateButton = Button(MainWindow,text="คำนวน")
calculateButton.bind('<Button-1>',leftClickButton)
calculateButton.grid(row=2,column=0)
labelResult = Label(MainWindow,text="ผลลัพธ์")
labelResult.grid(row=2,column=1)
MainWindow.mainloop()