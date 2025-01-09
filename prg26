#Use base class constructor and inheritance to display a book detail 
class Publisher:
    def __init__(self, name):
        self.name = name

class Book(Publisher):
    def __init__(self, name, title, author):
        super().__init__(name)
        self.title = title
        self.author = author

class Python(Book):
    def __init__(self, name, title, author, price, no_of_pages):
        super().__init__(name, title, author)
        self.price = price
        self.no_of_pages = no_of_pages

    def display(self):
        print(
            f"Publisher Name: {self.name}\n"
            f"Book Title: {self.title}\n"
            f"Book Author: {self.author}\n"
            f"Book Price: {self.price}\n"
            f"No. of Pages: {self.no_of_pages}"
        )

# Example usage
a = Python("Thomas", "Python Fundamentals", "Mark", 100, 200)
a.display()
