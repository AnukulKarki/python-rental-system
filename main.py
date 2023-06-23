
import view
import borrow
import Return

def main():
    """This function display the welcome screen of rental system and access
        all the modules require for the system"""
    print("==" * 20)
    print("\t Custom Rental Shop")
    print("==" * 20)
    while(True):
        print("Which option would you like to choose: \n \
        (1)    ||      View The Item\n \
        (2)    ||      Borrow The Item\n \
        (3)    ||      Return The Item\n \
        (4)    ||      Exit\n ")
        success = True
        while(success):
            try:
                option = int(input("Enter The Option You Would like to choose: "))
                success = False
            except:
                print("\nPlease Enter the Valid option\n")
        print()
        if(option == 1):
            print("Let's View The Item")
            #call the view function from view module
            view.view()
        elif(option == 2):
            print("Let's Rent The Item")
            #call the rentValidate function from the borrow module
            borrow.rentValidate()
            
        elif(option == 3):
            print("Let's Return The Item")
            #call teh rentIdValidate function from Return module
            Return.rentIdValidate()
            
        elif(option == 4):
            print("Thank You For Visiting Us")
            print("--"*20)
            #exit for the loop
            break
        else:
            print("Enter the valid the option\n")
            
main()
        
