import os

class Person:
    def __init__(self, name):
        self._name = name  

    @property
    def name(self):
        return self._name

class Librarian(Person):
    def __init__(self, name):
        super().__init__(name)

    def add_book(self, books, title, author):
        books.append({'title': title, 'author': author, 'status': 'доступна'})
        print(f"Книга '{title}' добавлена в систему.")

    def remove_book(self, books, title):
        for book in books:
            if book['title'] == title:
                books.remove(book)
                print(f"Книга '{title}' удалена из системы.")
                return
        print(f"Книга '{title}' не найдена.")

    def register_user(self, users, username):
        users.append({'name': username, 'borrowed_books': []})
        print(f"Пользователь '{username}' зарегистрирован.")

    def view_users(self, users):
        print("Список пользователей:")
        for user in users:
            print(f"Имя: {user['name']}, Взятые книги: {user['borrowed_books']}")

    def view_books(self, books):
        print("Список книг:")
        for book in books:
            print(f"книга {book['title']} от {book['author']} - Статус: {book['status']}")

class User(Person):
    def __init__(self, name):
        super().__init__(name)
        self.borrowed_books = []

    def view_available_books(self, books):
        print("Доступные книги:")
        for book in books:
            if book['status'] == 'доступна':
                print(f"книга {book['title']} от {book['author']}")

    def take_book(self, books, book_title, user):
        for book in books:
            if book['title'] == book_title:
                if book['status'] == 'доступна':
                    book['status'] = 'выдана'
                    user.borrowed_books.append(book['title'])
                    print(f"{user.name} взял книгу '{book_title}'.")
                    return
                else:
                    print("Эта книга уже выдана.")
                    return
        print("Книга не найдена.")

    def return_book(self, books, book_title, user):
        for book in books:
            if book['title'] == book_title:
                if book['title'] in user.borrowed_books:
                    book['status'] = 'доступна'
                    user.borrowed_books.remove(book['title'])
                    print(f"{user.name} вернул книгу '{book_title}'.")
                    return
                else:
                    print("У вас этой книги нет.")
                    return
        print("Книга не найдена.")

    def view_borrowed_books(self, user):
        print(f"{user.name}, ваши взятые книги: {user.borrowed_books}")

def load_books(file='books.txt'):
    books = []
    if os.path.exists(file):
        with open(file, 'r', encoding='utf-8') as f:
            for line in f:
                title, author, status = line.strip().split(';')
                books.append({'title': title, 'author': author, 'status': status})
    return books

def save_books(books, file='books.txt'):
    with open(file, 'w', encoding='utf-8') as f:
        for book in books:
            f.write(f"{book['title']};{book['author']};{book['status']}\n")

def load_users(file='users.txt'):
    users = []
    if os.path.exists(file):
        with open(file, 'r', encoding='utf-8') as f:
            for line in f:
                parts = line.strip().split(';')
                name = parts[0]
                borrowed = parts[1].split(',') if parts[1] else []
                users.append({'name': name, 'borrowed_books': borrowed})
    return users

def save_users(users, file='users.txt'):
    with open(file, 'w', encoding='utf-8') as f:
        for user in users:
            borrowed_str = ','.join(user['borrowed_books'])
            f.write(f"{user['name']};{borrowed_str}\n")

def main():
    books = load_books()
    users = load_users()

    print("Добро пожаловать в систему библиотеки!")

    role = input("Выберите роль (1 - Библиотекарь, 2 - Пользователь): ")

    if role == '1':
        librarian_name = input("Введите имя библиотекаря: ")
        librarian = Librarian(librarian_name)

        while True:
            print("\nВыберите действие:")
            print("1. Добавить книгу")
            print("2. Удалить книгу")
            print("3. Зарегистрировать пользователя")
            print("4. Просмотреть список пользователей")
            print("5. Просмотреть список книг")
            print("6. Выход")
            choice = input()

            if choice == '1':
                title = input("Название книги: ")
                author = input("Автор: ")
                librarian.add_book(books, title, author)
            elif choice == '2':
                title = input("Название книги для удаления: ")
                librarian.remove_book(books, title)
            elif choice == '3':
                username = input("Имя нового пользователя: ")
                librarian.register_user(users, username)
            elif choice == '4':
                librarian.view_users(users)
            elif choice == '5':
                librarian.view_books(books)
            elif choice == '6':
                break
            else:
                print("Некорректный выбор.")

    elif role == '2':
        username = input("Введите ваше имя: ")
        user = User(username)

        user_data = next((u for u in users if u['name'] == username), None)
        if user_data:
            user.borrowed_books = user_data['borrowed_books']
        else:
            users.append({'name': username, 'borrowed_books': []})

        while True:
            print("\nВыберите действие:")
            print("1. Просмотреть доступные книги")
            print("2. Взять книгу")
            print("3. Вернуть книгу")
            print("4. Просмотреть взятые книги")
            print("5. Выход")
            choice = input()

            if choice == '1':
                user.view_available_books(books)
            elif choice == '2':
                book_title = input("Название книги: ")
                user.take_book(books, book_title, user)
            elif choice == '3':
                book_title = input("Название книги для возврата: ")
                user.return_book(books, book_title, user)
            elif choice == '4':
                user.view_borrowed_books(user)
            elif choice == '5':
                for u in users:
                    if u['name'] == user.name:
                        u['borrowed_books'] = user.borrowed_books
                save_books(books)
                save_users(users)
                break
            else:
                print("Некорректный выбор.")
    else:
        print("Некорректный ввод. Завершение программы.")

    save_books(books)
    save_users(users)
    print("Данные сохранены. До свидания!")

if __name__ == "__main__":
    main()