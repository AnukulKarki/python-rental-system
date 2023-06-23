#importing the modules

import view
import datetime
import bill
#creating the global variable
customerName = ""
quantity:int
itemRented = []
fileName = ""
unixTimeStamp = None

def rentValidate():
    """This Function validate if the rent id is valid or not and call the other function if valid"""
    global itemRented
    global fileName
    global customerName
    global unixTimeStamp
    itemRented = []
    customerName = ""
    
    while True:
        view.view()
        isRented = False
        while True:
            try:
                rentId = int(input("\nEnter the id of the item you want to rent: "))
                break
            except:
                print("\nPlease Enter the Id in numeric form")

        for rentItem in range(len(itemRented)):
            if(int(itemRented[rentItem][1]) == rentId):
                print("\nItem Is already rented by the customer")
                print("\nPlease Rent The other costume")
                isRented = True
        if isRented:
            continue
        if(rentId > 0 and rentId<= len(view.itemDictionary)):
            if quantityValidate(rentId):
                renting(rentId)
            else:
                continue
        else:
            print("Please Select The Valid Id \n")
            continue
        
        print("User Want to buy more costume")
        useIn=input("Press Y to continue: ")
        if (useIn.lower()!="y"):
            customerTextFile()
            bill.customerBill(fileName,unixTimeStamp)
            break
        

        

def quantityValidate(rentId):
    """This Function validate if the quantity entered is valid and if yes then it return True"""
    global customerName
    global quantity

    if(int(view.itemDictionary[rentId][3]) == 0):
        print("\nItem Is not Available")
        return False
    else:
        print("++"*10)
        print("Costume Is Availabe")
        print("++"*10)

        
        while True:
            #try except to check the valid imput
            try:
                quantity = int(input("\nEnter the amount of item you want to rent"))
                break
            except:
                print("\nPlease Enter The Quantity In Numeric Form")
        
        if(quantity > int(view.itemDictionary[rentId][3])):
            print("\nWe have less than required amount")
            return False
        elif(quantity > 0 and quantity <= int(view.itemDictionary[rentId][3])):
            if customerName == "":
                success = True
                while(success):
                    customerName = input("\nEnter the name of the customer: ")
                    if(customerName.isalpha()):
                        success = False
                    else:
                        print("Use a valid customer name")
            return True
        else:
            print("Please Enter the valid Id")
            return False

def renting(rentId):
    """This function is used to rent the item that the user want to borrow"""
    global customerName
    global quantity
    

    #making the box for the item to be shown
    print("--"*35)
    print("Id\t Custome Name \t\tCustome Brand \t Price \t Quantity")
    print("--"*35,"\n")
    print(rentId,end="\t")

    for dataLength in range(len(view.itemDictionary[rentId])-1):
        if dataLength == 0 and rentId == 1:
            print(view.itemDictionary[rentId][dataLength],end="\t\t  ")
        else:
            print(view.itemDictionary[rentId][dataLength],end="\t  ")
    print(quantity)

    print("\n","--"*35,"\n")

    view.itemDictionary[rentId][3] = str(int(view.itemDictionary[rentId][3]) - quantity)

    price = view.itemDictionary[rentId][2]
    #replacing the $ to 0
    changePrice = price.replace("$","0")
    #calculating the total price for 5 days
    totalPrice = float(changePrice)*quantity
    print("\t\t\tTotal Charge:",totalPrice,"\n\n")
    #entering the data 
    itemRented.append(("Costume Id: ",str(rentId),",","Quantity: ",str(quantity),",","Price: ",str(totalPrice)))
    #calling the function to update text file
    itemUpdate()


def itemUpdate():
    """This text file update the item after renting or returning"""
    file = open("stock.txt","w")
    #loop in order to update all the value to the text file
    for values in view.itemDictionary.values():
        updatedData = ",".join(values)
        file.write(updatedData)
        file.write("\n")
    file.close()

def customerTextFile():
    """This function creates a text file after the user borrow the item"""
    global customerName
    global fileName
    global unixTimeStamp
    unixTimeStamp = 0
    date = datetime.datetime.now()
    #generating the unix time inorder to get the unique ID 
    unixTimeStamp=str(int(datetime.datetime.timestamp(date)))
    fileName = customerName+unixTimeStamp+".txt"
    #opeaning the files
    file = open(fileName,"w")
    file.write("Invoice Id: %s"%(unixTimeStamp))
    file.write("\n")
    file.write("Customer Name: %s"%customerName)
    file.write("\n")
    file.write("Date: %s"%(str(date)))
    file.write("\n")
    file.write("\n")
    file.write("--"*16)
    file.write("\n")
    for i in itemRented:
        file.write("".join(i))
        file.write("\n")
    file.write("--"*16)
    #closing the file
    file.close()




    




    
    


    



