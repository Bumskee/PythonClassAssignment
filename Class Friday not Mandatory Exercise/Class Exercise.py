class Author:
    def __init__(self, name, email, gender):
        self.__name = name
        self.__email = email
        self.__gender = gender

    def getName(self):
        return self.__name

    def getEmail(self):
        return self.__email

    def getGender(self):
        return self.__gender

    def setEmail(self, email):
        self.__email = email

    def toString(self):
        return (f"Author[Name = {self.__name}, Email = {self.__email}, Gender = {self.__gender}]")

class Book(Author):
    def __init__(self, name, authors, price, qty):
       self.__name = name
       if type(authors) == list:
           self.__authors = authors
       else:
           self.__authors = [authors]
       self.__price = price
       self.__quantity = qty  

    def getAuthors(self):
        return self.__authors

    def getAuthorsInfos(self):
        temp = []
        for i in self.__authors:
            temp += [i.toString()]
        return ', '.join(temp)

    def getAuthorsNames(self):
        temp = []
        for i in self.__authors:
            temp += [i.getName()]
        return ', '.join(temp)

    def getAuthorsEmails(self):
        temp = []
        for i in self.__authors:
            temp += [i.getEmail()]
        return ', '.join(temp)

    def getAuthorsGenders(self):
        temp = []
        for i in self.__authors:
            temp += [i.getGender()]
        return ', '.join(temp)

    def getPrice(self):
        return self.__price

    def getQty(self):
        return self.__quantity

    def setPrice(self, price):
        self.__price = price
        
    def setQty(self, qty):
        self.__quantity = qty

    def toString(self):
        return (f"Book[Name = {self.__name}, {self.getAuthorsInfos()}, " + f"Price = {self.__price}, Quantity = {self.__quantity}.")


Andi = Author("Andy James", "Jameskii@ymail.com", "m")
Dodi = Author("Dodi Adikusumah", "DodiGantengs@bonus.com", "m")
TestBook = Book("The Legend of The Cursed Lost Ship of The Lost Atlantean Culture from The Lost Archipelago of The Lost Continent of Atlantis", [Andi, Dodi], 50000, 2)
print(TestBook.toString())