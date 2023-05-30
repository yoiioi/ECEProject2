from Book import Book

"""create new arrrays with loist of titles
add= update to the array
extract titls from the array at method add
"""
class Inventory:
    def __init__(self):
        self.items=[]
        
    def initialize(self):
        self.items=[
            Book("A Brief History of Time","Stephen Hawking",10.17,"GV5N32M9"),
            Book("The Alchemist","P. Coelho",6.99,"TR3FL0EW"),
            Book("Thus Spoke Zarathustra","F. Nietzsche",7.81,"F2O9PIE9"),
            Book("Jonathan Livingston Seagull","R. Bach",6.97,"R399CED1"),
            Book("The Time Machine","H. G. Wells",5.95,"6Y9OPL87"),
            Book("Introduction to Programming in Python","R. Sedgewick",69.99,"5T3RRO90"),
            Book("Atoms of Silence","H. Reeves",28.02,"3W2TB162"),
            Book("2001: A Space Odyssey","A. C. Clarke",8.99,"TU2RL012"),
            Book("20,000 Leagues under the Sea","J. Verne",5.99,"JI2PL986"),
            Book("Les Miserables","V. Hugo",9.98,"VC5CE249")
        ]
    def __str__(self):
        booklist="" #initilaizing book list
        for i in range(len(self.items)): #assigning book ID (i+1)
            booklist=booklist+str(i+1)+" - "+str(self.items[i])+"\n" #storing the informations in the book list
        return booklist #returnig to the "Inventory"
    
    #Option 2: Info Inventory
    def info(self):
        print("#Items: "+str(len(self.items))) #counting the length of list "items"
        total_price=sum(book.price for book in self.items)
        print("Total price $"+str(total_price))
        max_price= max(book.price for book in self.items) #evaluating the maximum price comparing with all the list of books
        print("Most expensive item at $"+str(max_price))

    #Option 3: Search Inventory
    def search(self, keyword):
        results=[] #empty array of results
        id=[] #records the book id 
        for i in range(len(self.items)):
            if keyword.lower() in self.items[i].title.lower(): #lower case for accurate search
                results.append(self.items[i]) #add book to the results when it contains the keyword
                id.append(i+1) #keep track of id as well
        if len(results)==0:
            print("No book found!")
        else:
            for i in range(len(results)):
                print(str(id[i])+" - "+str(results[i])) #print info using both lists
    
    #Option 4: Add Item
    def add(self,book_id=None): #make book id optional
        if book_id is None:
            new_title=input("Enter Title: ")
            new_author=input("Enter Author Name: ")
            new_price=input("Enter Price: ")
            new_reference=input("Enter Reference: ")
            self.items.append(Book(new_title,new_author,float(new_price),new_reference))
        else:
           self.items.append(book_id) #appending the items


    #Option 6
    def adjust_price(self,rate):
        for i in self.items:
            i.price *=(1+(rate/100))
