class Animal:
    def eat(self):
        print("Eating Eating!")

class Cat(Animal):
    def eat(self):
        print("Meoww !!") 

cat1 = Cat()
cat1.eat() # ทับ function แม่ได้

animal1 = Animal()
animal1.eat()