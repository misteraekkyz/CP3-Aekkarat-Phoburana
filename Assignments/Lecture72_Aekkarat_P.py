menuList = []
def showBill():
    totalprice = 0
    print("--- MisterA Shop ---")
    for number in range(len(menuList)):
        print(menuList[number][0],menuList[number][1])
        totalprice += int(menuList[number][1])
    print("Total is : ",totalprice, "THB")

while True :
    menuName = input("Plese Enter Menu : ")
    if(menuName.lower() == "exit"):
        break
    else:
        menuPrice = input("Price : ")
        menuList.append([menuName,menuPrice])

showBill()