


itemDictionary = {}

def itemAccess():
    """This function helps to access the items from the text file"""
    global itemDictionary
    #open the text to access the stock
    itemFile = open("stock.txt","r")
    costumeData = itemFile.read().split("\n")

    #loop to remove the empty data from the list
    while("" in costumeData):
        costumeData.remove("")
    
    idNumber = 0
    #loop for entering the data in the dictionary
    for length in range(len(costumeData)):
        idNumber += 1
        itemDictionary[idNumber] = costumeData[length].split(",")


def display():
    """This function helps to display the item that
        are present in the asthetic way"""
    global itemDictionary
    print("--"*35)
    print("Id\t Custome Name \t\t Custome Brand \t Price \t Quantity")
    print("--"*35,"\n")
    #initalizing the loops for the item dicitonary
    for idNum in itemDictionary.keys():
        print(idNum,end="\t")
        for dataLength in range(len(itemDictionary[idNum])):
            if dataLength == 0 and idNum == 1:
                print(itemDictionary[idNum][dataLength].strip(),end="\t\t  ")
            else:
                print(itemDictionary[idNum][dataLength].strip(),end="\t  ")
            
        print("\n")
    print("--"*35)

def view():
    """This function runs both function"""
    itemAccess()
    display()






