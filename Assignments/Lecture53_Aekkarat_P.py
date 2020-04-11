def vatCalculator(totalPrice):
    result = totalPrice+(totalPrice*7/100)
    return result

Price = int(input("Enter Price : "))
print("Total is : ",vatCalculator(Price))
