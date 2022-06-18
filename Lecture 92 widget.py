from tkinter import * # ไม่ต้องเขียน math.other ลดเวลาการเขียน

def sayHelloWorld():
   print("Hello World")

MainWindow = Tk() # สร้าง mainWindow ขึ้นมาก่อน 1 อัน : สร้างหน้าต่างขึ้นมา
button = Button(MainWindow,text = "Click me",command = sayHelloWorld) 
button.place(x = 50, y = 20)
MainWindow.mainloop() # เรียกใช้เพื่อให้มันทำงาน