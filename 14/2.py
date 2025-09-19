class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def display(self):
        print("Title:", self.title)
        print("Author:", self.author)
        print("Price:", self.price)

    def apply_discount(self, percent):
        self.price -= self.price * (percent / 100)

b1 = Book("Python Basics", "John Smith", 500)
b2 = Book("Data Science", "Alice Brown", 800)

b1.display()
b2.display()

b1.apply_discount(10)
b1.display()
