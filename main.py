# exercise 1:

def count_vowels(text):
    if not isinstance(text, str):  # isinstance to check the type
        return 42

    count = 0
    vowels = 'aeiou'
    for character in text.lower():
        if character in vowels:
            count += 1

    return count


print(count_vowels('AHhhAhaA'))


# exercise 2:

def hamming(text1, text2):
    if len(text1) != len(text2):
        return 0
    else:
        count = 0
        for index in range(0, len(text1)):
            if text1[index] == text2[index]:
                count += 1
        return count


print(hamming('dog', 'cat'))


# exercise 3:

class Vehicle:
    def __init__(self, color: str, fuel_type: str):
        self.color = color
        self.fuel_type = fuel_type


class Car(Vehicle):
    def __init__(self, color: str, fuel_type: str, doors: int):
        super().__init__(color, fuel_type)
        self.doors = doors

    def __str__(self):
        return f"Color: {self.color}, Fuel Type: {self.fuel_type}, Doors: {self.doors}"


class Bus(Vehicle):
    def __init__(self, color: str, fuel_type: str, passengers: int):
        super().__init__(color, fuel_type)
        self.passengers = passengers

    def __str__(self):
        return f"Color: {self.color}, Fuel Type: {self.fuel_type}, Passengers: {self.passengers}"


car = Car("green", "oil", 4)
print(car)

bus = Bus('red', 'solar power', 23)
print(bus)


# exercise 4:

class Book:
    def __init__(self, name: str, author: str):
        self.name = name
        self.author = author

    def __str__(self):
        return f"{self.name}, {self.author}"

    def __repr__(self):
        return f"Book('{self.name}', '{self.author}')"


book1 = Book('Artemis Fowl', 'Eoin Colfer')
print(book1)


# exercise 5:

class BookShelf:
    def __init__(self):
        self.my_books = []

    def add_book_list(self, books: list[Book]):
        for book in books:
            if isinstance(book, Book):
                self.my_books.append(book)

    def books_by_author(self, author):
        result = []
        for book in self.my_books:
            if book.author == author:
                result.append(book.name)
        return result

    def get_books(self):
        result = []
        for book in self.my_books:
            result.append(book.name)
        return result

    def clear_shelf(self):
        self.my_books.clear()


book_shelf = BookShelf()

book_list_1 = [Book("Artemis Fowl", "Eoin Colfer"), Book("Six of Crows", "Leigh Bardugo")]
book_shelf.add_book_list(book_list_1)

book_list_2 = [Book("Plugged", "Eoin Colfer"), 'porcelain turtle']
book_shelf.add_book_list(book_list_2)

print(book_shelf.my_books)
print(book_shelf.books_by_author("Eoin Colfer"))
print(book_shelf.clear_shelf())
print(book_shelf.get_books())
