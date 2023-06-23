#import datetime
import datetime

def returnTextFile(customerName,invoiceId, item,rentCostume, totalPrice):
    """This function helps to generate the text file after the item has been returned"""
    global customerTextFile
    itemList = []
    second = datetime.datetime.now().second
    #creating the unique return text file name
    returnTextFile = "return_"+str(second) + customerName + invoiceId + ".txt"
    file = open(returnTextFile,"w")
    file.write("Customer Name: %s"%customerName)
    file.write("\n")
    file.write("Invoice Id: %s"%invoiceId)
    file.write("\n")
    file.write("Date of Rent: %s"%(str(item[3][0].split(" ")[1])))
    file.write("\n")
    file.write("Date of Return: %s"%(datetime.datetime.now()))
    file.write("\n")
    file.write("=="*15)
    file.write("\n")
    cycleComplete = False
    #loop for entering the data in the text file
    for length in range(len(rentCostume)):
        if (cycleComplete == True):
            itemList = []
        if(length % 2 == 0):
            itemList.append("Rent Id: "+str(int(rentCostume[length])))
            cycleComplete = False
        else:
            itemList.append("Quantity: "+ str(int(rentCostume[length])))
            cycleComplete = True  
        if(cycleComplete == True):
            file.write(",".join(itemList))
            file.write("\n")
    file.write("Total Price: %s"%("$"+str(totalPrice)))
    file.write("\n")
    file.write("=="*15)
    #closing the file
    file.close()
