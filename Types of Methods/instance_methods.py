'''
Challenge/Task:

1. Define a class Book with attributes title and author.
2. Create an instance method display_info that prints the book's title and author.
3. Instantiate the Book class and call the display_info method.
'''

# define the class book 
class Book:
    # initialization of attributes title and author
    def __init__(self, title, author):
        self.title = title
        self.author = author

    # method that prints book's title and author
    def display_info(self):
         print(f"Book\'s title: {self.title}")
         print(f"Book\'s Author: {self.author}")

def main():
    # instantiate the book class 
    book_1 = Book(title="Harry Potter and the Prisoner of Azkaban", author="J. K. Rowling")
    # call the display_info method
    book_1.display_info()

if __name__ == "__main__":
    print("Book Details: ")
    main()