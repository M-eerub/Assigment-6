# step 11 (Class Methods)

class Books:
    total_books = 0

    @classmethod
    def Increament_books(cls):
        cls.total_books += 1

Books.Increament_books()
Books.Increament_books()
Books.Increament_books()
print(Books.total_books)
