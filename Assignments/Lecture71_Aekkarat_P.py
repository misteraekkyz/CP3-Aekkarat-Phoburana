menuList = []
priceList = []

def showBill():
    totalprice = 0
    print("--- MisterA Shop ---")
    for number in range(len(menuList)):
        print(menuList[number],priceList[number])
        totalprice += int(priceList[number])
        print("Total price is : ",totalprice,"THB")

while True :
    menuName = input("Plese Enter Menu : ")
    if(menuName.lower() == "exit"):
        break
    else :
        menuPrice = input("Price : ")
        menuList.append(menuName)
        priceList.append(menuPrice)
print(menuList,priceList)
print("Total is : ",priceList)
showBill()