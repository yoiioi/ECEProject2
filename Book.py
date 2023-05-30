class Book:

    def __init__(self,title,author,price,reference): #Constructor defining attributes
        self.reference=reference
        self.title=title
        self.author=author
        self.price=price
    def __str__(self):
       return "Title: %s; Author: %s; (Ref: %s; Price: $%s)"%(self.title,self.author,self.reference,self.price)
    def get_title(self):
        return self.title

    
def main():
    book1=Book("A Brief History of Time","Stephen Hawking",10.17,"GV5N32M9")
    print(book1)
    book2=Book("The Alchemist","P. Coelho",6.99,"TR3FL0EW")
    book3=Book("Thus Spoke Zarathustra","F. Nietzsche",7.81,"F2O9PIE9")
    book4=Book("Jonathan Livingston Seagull","R. Bach",6.97,"R399CED1")
    book5=Book("The Time Machine","H. G. Wells",5.95,"6Y9OPL87")
    book6=Book("Introduction to Programming in Python","R. Sedgewick",69.99,"5T3RRO90")
    book7=Book("Atoms of Silence","H. Reeves",28.02,"3W2TB162")
    book8=Book("2001: A Space Odyssey","A. C. Clarke",8.99,"TU2RL012")
    book9=Book("20,000 Leagues under the Sea","J. Verne",5.99,"JI2PL986")
    book10=Book("Les Miserables","V. Hugo",9.98,"VC5CE249")

if __name__=="__main__":
    main()
