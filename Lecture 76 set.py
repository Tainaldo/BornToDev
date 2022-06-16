userInput = int(input("Enter Number of Your Favorites Fruits :"))
myFruits = set() #สร้าง set เก็บผลไม้ที่เราชอบ
while (len(myFruits) < userInput): # len ไว้ดูขนาด
    myFruits.add(input("Fruist : "))
    print(myFruits)