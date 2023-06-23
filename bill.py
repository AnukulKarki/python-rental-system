#importing the modules

import view
import datetime
def customerBill(fileName,unixTimeStamp):
    """This functions helps to a bill after renting"""
    
    file = open(fileName,"r")
    fileDetail = file.read().split("\n")

    
    while("" in fileDetail):
        fileDetail.remove("")

    item = {}
    count = 0
    for length in fileDetail:
        count += 1
        item[count] = length.split(",")

    itemList = []
    brandList = []
    totalPrice = 0
    print("\n\n"+"--"*30)
    print("\t\tCustome Bill")
    print("--"*30)
    print("**"*30)
    print("Name of the customer:",item[2][0].split(" ")[2])
    print("Invoice Id: ",unixTimeStamp)
    print("Date Time of borrow:",item[3][0].split(" ")[1])
    #creating the loop to access all the data
    for keys in item.keys():
        if(keys > 4 and keys < len(item)):
            itemList.append(view.itemDictionary[int(item[keys][0].split(" ")[2])][0])
            
            brandList.append(view.itemDictionary[int(item[keys][0].split(" ")[2])][1])
            
            quantity = int(item[keys][1].split(" ")[1])

            
            price = view.itemDictionary[int(item[keys][0].split(" ")[2])][2]
            changePrice = price.replace("$","0")
            totalPrice += float(changePrice) * quantity
    
    print("Total Price: ","$"+str(totalPrice))
    print("Items:",itemList)
    print("Brands:",brandList)
    print("--"*30,"\n")
    print("\n"+"--"*15)
    print("|   Bill has been generated |")
    print("--"*15,"\n\n")

def customerFinalBill(totalPrice,rentCostume,item):
    """This function helps to make a bill after returning the item"""
    itemList = []
    itemBrand = []
    print("\n\n"+"--"*30)
    print("\t\tCustome Bill")
    print("--"*30)
    print("**"*30)
    print("Name of the customer:",item[2][0].split(" ")[2])
    print("Date Time of borrow:",item[3][0].split(" ")[1])
    print("Date Of Return:",datetime.datetime.now())
    #create a loop to access the data
    """It checks the place where the costume id is
        availeble and access those file in it"""
    for length in range(len(rentCostume)):
        if(length % 2 == 0):
            itemList.append(view.itemDictionary[int(rentCostume[length])][0])
            itemBrand.append(view.itemDictionary[int(rentCostume[length])][1])
    print("Item Returned:",itemList)
    print("Brand Returned:",itemBrand)
    print("Your Total Price: ","$"+str(totalPrice))
    print("**"*30,"\n\n")
    
    print("\tThank you for choosing us\n\n")
