

class Book:
    _id_counter = 1

    def __new__(cls, *args, **kwargs):
        instance = super().__new__(cls)
        instance.id = cls._id_counter
        cls._id_counter += 1

        return instance


    def __init__(self, title, author):
        self.title = title
        self.author = author


    def __str__(self):
        return f"Book(ID = {self.id}, title = {self.title}. author = {self.author})"



if __name__ == '__main__':
    book1 = Book('The Da Vinci Code', 'Dan Brown')
    book2 = Book('Origin', 'Dan Brown')
    print(book1)
    print(book2)