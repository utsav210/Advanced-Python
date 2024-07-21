'''
Challenge:

1. Define a class Library with a class attribute total_books.
2. Create a class method update_total_books that updates the total_books attribute.
3. Call the class method to modify the class attribute.
'''
# defined the class library
class Library:
    total_books = 0 # class attribute
    
    @classmethod
    def update_total_books(cls, number):
        cls.total_books += number
        print(f"Total Books updated to: {cls.total_books}")

lib = Library()

def main():
    # display the initial total books:
    print(f"Initial total books are: {lib.total_books}")

    # call the class method to update the total_books
    lib.update_total_books(2) # adds 2 books
    lib.update_total_books(5) # adds more 5 books
    lib.update_total_books(15) # adds more 15 books

    # display updated total books
    print(f"Final Updated total books: {lib.total_books}")

if __name__ == "__main__":
    main()
