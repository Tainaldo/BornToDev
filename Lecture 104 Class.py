class Customer:
    name = ""  # name คือ Attribute
    lastname = ""
    age = 0 # ให้ 0 เป็นค่าเริ่มต้น
    def addCart(self):
        print("Add to",self.name,self.lastname)

customer1 = Customer() # เรียกใช้งาน Function
customer1.name = "Tai"
customer1.lastname = "Jaikla"
customer1.age = 10
customer1.addCart()