class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

# function to display book information
    def display_info(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Year: {self.year}")

    def __str__(self):
        return f"'{self.title}' by {self.author} ({self.year})"

# inheritance
class EBook(Book):
    def __init__(self, title, author, year, file_size):
        super().__init__(title, author, year)
        self.file_size = file_size

    def display_info(self):
        super().display_info()
        print(f"File Size: {self.file_size} MB")

    def __str__(self):
        return f"'{self.title}' by {self.author} ({self.year}) - EBook ({self.file_size} MB)"

# Example usage
title = input("Enter book title: ")
author = input("Enter book author: ")
year = int(input("Enter book year: "))
file_size = float(input("Enter eBook file size (MB): "))
print("\n")
print("Display Book Information:")
print("-------------------------")

# creating a base Book
Book1 = Book(title, author, year)
Book1.display_info()
print("\n")
# creating an EBook
EBook1 = EBook(title, author, year, file_size)
EBook1.display_info()
print(Book1)