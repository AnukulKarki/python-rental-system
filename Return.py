#imporing the modules
import datetime
import view
import borrow
import bill
import returnTextFile

#creating the global vaiable

item = {}
quantity:int
customerTextFile = ""
rentCostume = []
totalPrice = 0



def customerTextFileUpdate():
    """This function helps to update the text file after return"""

    #getting the access to the global variable
    global item
    global customerTextFile
    file = open(customerTextFile,"w")
    for keys in item.keys():
        if(keys <=3):
            file.write(item[keys][0])
            file.write("\n")
        else:
            join = ",".join(item[keys])
            file.write(join)
            file.write("\n")
def itemAccessReturn():
    """this function helps to access the data that are rented"""
    global customerTextFile
    global item
    #opeaning the text file in read mode
    file = open(customerTextFile,"r")

    fileDetail = file.read().split("\n")

    #removing the white space
    while("" in fileDetail):
        fileDetail.remove("")
    count = 0
    #inserting the data to the dictionary
    for length in fileDetail:
        count += 1
        item[count] = length.split(",")

def rentIdValidate():
    """This function helps to check wheather the rentID is validated or not"""
    global totalPrice
    global rentCostume
    rentCostume = []
    totalPrice = 0
    global customerTextFile
    #check if the name is valid
    while(True):
        try:
            while(True):
                customerName = input("Enter the name of the customer: ")
                if(customerName.isalpha()):
                    break
                else:
                    print("Use a valid customer name")
            #check if the id is written in numeric form
            while(True):
                try:
                    invoice = str(int(input("Please Enter the invoice Id: ")))
                    break
                except:
                    print("\nInvalid ID! Enter Again\n")

            customerTextFile = customerName+invoice+".txt"
            #accesing the item from the renting file
            itemAccessReturn()
            break
        except:
            print("Customer File Not Found")





    
    while(True):
        while(True):
            notValidate = False
            print("\n\tRented Items\n")
            print("=="*15)
            for keys in item.keys():
                if(keys > 4 and keys < len(item)):
                    print(item[keys][0],"\t",item[keys][1])
            print("\n"+"=="*15)
            #check if the id is valid number or not
            try:
                returnRentId = int(input("\nEnter the id you want to return: "))
                break
            except:
                print("\nPlease Enter the valid id")
        if returnRentId < 0:
            print("Please Enter the valid id")
            continue
        counter = 0
        if(len(item) > 4):
            for keys in item.keys():
                if(keys > 4 and keys < len(item)):
                    if(returnRentId == int(item[keys][0].split(" ")[2])):
                        if(quantityValidateReturn(keys)):
                            Return(keys)
                        else:
                            notValidate = True
                        break
                    else:
                        counter += 1
            if(counter == len(item)-5):
                print("Item Not Found")
                continue
        else:
            print("Item is already returned")
        
        print("Do You want to return again")
        userInput = input("Press Y to enter yes: ")
        if(userInput.lower() == "y"):
            #continue the loop affter the user pressing the Y
            continue
        else:
            if(len(rentCostume) != 0):
                #call the customerFinalBill to genrate the bill
                bill.customerFinalBill(totalPrice,rentCostume,item)
                returnTextFile.returnTextFile(customerName,invoice, item,rentCostume, totalPrice)
            else:
                print("\nItem is not Returned\n")
                print("=="*10)
            break

def quantityValidateReturn(keys):
    """This function helps to validate the quantity"""
    global item
    global quantity
    if(int(item[keys][1].split(" ")[1]) == 0):
        print("\nItem is not available to return\n")
        return False
    else:
            
        while(True):
            #try except to get the valid input
            try:
                quantity = int(input("\nEnter the quantity: "))
                break
            except:
                print("\nPlease Enter the valid quantity\n")
        if(quantity > int(item[keys][1].split(" ")[1])):
            print("\n Item rented is less than given amount\n")
            return False
        elif(quantity > 0 and quantity <= int(item[keys][1].split(" ")[1])):
            #return the true value if validated
            return True

        else:
            print("\nPlease Enter the valid quantity")
            #return the false value if the quantity is not valid
            return False


def Return(keys):
    """This function helps to return the item that has been rented"""
    global quantity
    global rentCostume
    global totalPrice
    date = datetime.datetime.now()
    returnTime = int(datetime.datetime.timestamp(date))
    rentDay = int(item[1][0].split(" ")[2])
    #checking if the day crossed 5 days or not
    Days = int((returnTime-rentDay)/86400)
    """
    Unix Time has been used in order to check if the 5 5 days mark has crossed or not
    This also helped to create the unique id
    """
    if(Days>5):
        print("\nFine is charged for $1 per day")
        noOfDays = Days
    else:
        noOfDays = 0
    view.itemAccess()
    #accessing the price
    print("\nItem Is Returned")
    print("================================")
    print(view.itemDictionary[int(item[keys][0].split(" ")[2])][0])
    print("================================")
    #getting the price of the item
    price = view.itemDictionary[int(item[keys][0].split(" ")[2])][2]
    
    changePrice = price.replace("$","0")
    #calculating the total price 
    totalPrice += (float(changePrice) * quantity) + float(changePrice)/5*noOfDays + 1*noOfDays
    #Adding the quantity in the main dictionary
    view.itemDictionary[int(item[keys][0].split(" ")[2])][3] =  str(int(view.itemDictionary[int(item[keys][0].split(" ")[2])][3])+ quantity)
    #updating the item in the main stock
    borrow.itemUpdate()
    
    rentCostume.append(item[keys][0].split(" ")[2])
    rentCostume.append(str(quantity))
    #updating the quantity 
    item[keys][1] ="Quantity: "+ str(int(item[keys][1].split(" ")[1]) - quantity)
    #updating the text file
    customerTextFileUpdate()
    

    
    
    
    



