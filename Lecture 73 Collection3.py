systemMenu = {"ข้าวหมกไก่":40 , "ข้าวมันไก่":40 , "ข้าวไก่ผสม":50 , "ข้าวมันไก่พิเศษ":45}
menuList = []

def showBill():
    print("---- My Food ----")
    totoalPrice = 0
    for food in range(len(menuList)):
        print(menuList[food][0],menuList[food][1])
        totoalPrice += menuList[food][1]
    print("-----------------")
    print("ราคาทั้งหมด",totoalPrice,"บาท")
        

while True: 
    menuName = input("Please Enter Menu :")
    if (menuName.capitalize() == "Exit"): 
        break
    else:
        menuList.append([menuName,systemMenu[menuName]])
print(menuList)
showBill()