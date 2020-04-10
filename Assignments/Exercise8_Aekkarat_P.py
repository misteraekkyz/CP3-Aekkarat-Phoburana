correct_username = "MisterA"
correct_password = "1234"

username= input("Username : ")
password = input("Password : ")
BN = 8
OG = 7
AD = 11
WL = 45
PA = 32
CN = 12

if correct_username == username and correct_password == password :
    print("Login Success!")
    print("--- Welcome To MisterA Shop ---")
    print(" 1.Banana     : 8 (THB) ")
    print(" 2.Orange     : 7 (THB) ")
    print(" 3.Avocado    : 11 (THB) ")
    print(" 4.Watermelon : 45 (THB) ")
    print(" 5.Pineapple  : 32 (THB) ")
    print(" 6.Coconut    : 12 (THB) ")
    fruitSelected = int(input(">> : "))
    if fruitSelected == 1 :
        amout = int(input("Amout the Product : "))
        price = amout * BN
        print("Banana Price :",price,"THB")
    elif fruitSelected == 2 :
        amout = int(input("Amout The Product : "))
        price2 = amout * OG
        print("Orange Price :",price2,"THB")
    elif fruitSelected == 3 :
        amout = int(input("Amout The Product : "))
        price3 = amout * AD
        print("Avocado Price :",price3,"THB")
    elif fruitSelected == 4 :
        amout = int(input("Amout The Product : "))
        price4 = amout * WL
        print("Watermelon Price :",price4,"THB")
    elif fruitSelected == 5 :
        amout = int(input("Amout The Product : "))
        price5 = amout * PA
        print("Pineapple Price :",price5,"THB")
    elif fruitSelected == 6 :
        amout = int(input("Amout The Product : "))
        price6 = amout * CN
        print("Coconut Price :",price6,"THB")
    print("----- Thank you for choosing us ----- ")
else :
    print("Login Not Success!")

