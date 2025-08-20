class Book:
    def __init__(self, title, author, genre, teg):
        self.title = title
        self.author = author
        self.genre = genre
        self.teg = teg

    def display_info(self):
        print(f"Название: {self.title};\n Автор: {self.author};\n Жанр: {self.genre};\n Теги: {self.teg}")

teg = ["Мистика", "Философия", "историческая фантазия"]
genre = ["Роман", "Сатира", "Фантастика"]
book_favorite = Book("Мастер и Маргарита", "М.Булгаков", genre, teg)
book_favorite.display_info()