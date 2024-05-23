class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn

    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}"

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def save_to_file(self, filename):
        try:
            with open(filename, 'w') as file:
                for book in self.books:
                    file.write(f"{book.title},{book.author},{book.isbn}\n")
            print("Library data successfully saved to file.")
        except IOError:
            print("Error saving library data to file.")

    @classmethod
    def load_from_file(cls, filename):
        library = cls()
        try:
            with open(filename, 'r') as file:
                for line in file:
                    title, author, isbn = line.strip().split(',')
                    library.add_book(Book(title, author, isbn))
            print("Library data successfully loaded from file.")
            return library
        except FileNotFoundError:
            print("File not found. Creating a new empty library.")
            return library
        except IOError:
            print("Error reading from file. Creating a new empty library.")
            return library

# Example usage
my_library = Library()
my_library.add_book(Book(" The Seven Deadly Sins", "Nakaba Suzuki", "9780439708180"))
my_library.add_book(Book("Dragonball Series", "Akira Toriyama", "9780061120084"))
my_library.add_book(Book("Kaiju 8", "Naoya Matsumoto", "9780451524935"))

# Save library to file
my_library.save_to_file("library_data.txt")

# Load library from file
loaded_library = Library.load_from_file("library_data.txt")

# Display loaded library
for book in loaded_library.books:
    print(book)
