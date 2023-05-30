###############################
# Team members- Please enter your names here
# Name1: Katherine Gayeon Kim
# Name2: 
###############################

# Modules
from Inventory import Inventory
inventory=Inventory()
inventory.initialize()
cart=Inventory()

def display_menu():
    print("""-------------------------------------------------------""")
    print("1-List Inventory; 2-Info Inventory; 3-Search Inventory;")
    print("4-Add Item; 5-Remove Item; 6-Inflation; 7-Shop; 8-Check-out\n")

'''------------------------------------------------------
                Main program starts here 
---------------------------------------------------------'''
# to complete
print("\nWelcome to BestMedia") #display all current polynomials
print("====================")
while True:
    display_menu()          #menu that contains all the options
    command=input("Enter Command: ")

    if command=="":         #exit program      
        print("Goodbye!")
        break

    elif command=="1":        #Option 1: List Inventory
        print(inventory)

    elif command=="2":        #Option 2: Info Inventory
        inventory.info()

    elif command=="3":        #Option 3: Search Inventory
        keyword=input("Enter a title keyword: ")
        inventory.search(keyword)

    elif command=="4":        #Option 4: Add Item
        inventory.add()
        
    elif command=="5":        #Option 5: Remove Item
        num=int(input("Which item do you want to delete: "))
        del inventory.items[num-1]

    elif command=="6":        #Option 6: Inflation
        rate=float(input("Enter Inflation %: "))
        inventory.adjust_price(rate)

    elif command=="7":        #Option 7: Shop
        book_id=int(input("Which item do you want to buy? "))
        if 0<= book_id < len(inventory.items): #setting up range for input
            book_to_buy=inventory.items[book_id-1] #storing the information about the book
            cart.add(book_to_buy) #adding to the cart by using add method
            print("\""+str(book_to_buy.title)+"\" added to shopping cart!")
        else:
            print("Invalid item ID. Please try again.") #avoiding program to crash

    elif command=="8": #Option 8: Check-out
        if (len(cart.items)) == 0: #does not proceed checkout when the cart is empty
            print("Your cart is empty!")
        else:
            print(cart)
            cart.info()
            promo_=input("Enter promotion code if any: ")
            promo=promo_.lower() #lower case for promo code to avoid errors
            if promo == "voyage":  
                cart.adjust_price(-5) #adjusting the price
                print("Updated shopping cart:")
                print(cart) #displaying updated info
                cart.info()
            elif promo == "parfait":
                cart.adjust_price(-10) #adjsting the price
                print("Updated shopping cart:")
                print(cart) #displaying updated info
                cart.info()
            card=input("Enter your credit card number: ") #taking in the credit card number
            print("Purchase done! Enjoy your new books")
            cart=Inventory() #resetting the cart



        
