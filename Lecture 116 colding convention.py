# Coding Convention
# การตั้งชื่อตัวแปร
user_age = 12
user_weght = 52
user_hight = 172
user_age = 22

# การตั้งชื่อฟังก์ชั่น
def say_hello():
    print("Hello")

say_hello1 = say_hello()

# การตั้งชื่อ class
class CustomerApp:
    name = ""  # name คือ Attribute
    lastname = ""
    age = 0 # ให้ 0 เป็นค่าเริ่มต้น
    def addCart(self):
        print("Add to",self.name,self.lastname)


customer1 = CustomerApp() # เรียกใช้งาน Function # เว้นจาก class 2 บรรทัด
customer1.name = "Tai"
customer1.lastname = "Jaikla"
customer1.age = 10
customer1.addCart()