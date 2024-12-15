books = [
    {"book_id": 1, "title": "Остров сокровищ", "author": "Роберт Стивенсон", "available": "В наличии", "genre": "роман", "evaluation": 4.8},
    {"book_id": 2, "title": "Властелин Колец", "author": "Джон Толкин", "available": "В наличии", "genre": "фентези", "evaluation": 5.0},
    {"book_id": 3, "title": "Евгений Онегин", "author": "Александр Пушкин", "available": "Нет в наличии", "genre": "роман в стихах", "evaluation": 4.4},
    {"book_id": 4, "title": "Гамлет, принц датский", "author": "Уильям Шекспир", "available": "В наличии", "genre": "трагедия", "evaluation": 5.0},
    {"book_id": 5, "title": "Мастер и Маргарита", "author": "Михаил Булгаков", "available": "Нет в наличии", "genre": "роман", "evaluation": 4.2},
    {"book_id": 6, "title": "Герой нашего времени", "author": "Михаил Лермонтов", "available": "В наличии", "genre": "роман", "evaluation": 4.7},
    {"book_id": 7, "title": "Хоббит", "author": "Джон Толкин", "available": "В наличии", "genre": "фентези", "evaluation": 5.0},
    {"book_id": 8, "title": "Илон Маск", "author": "Илон Маск", "available": "В наличии", "genre": "биография", "evaluation": 4.1},
    {"book_id": 9, "title": "1984", "author": "Джордж Оруэлл", "available": "Нет в наличии", "genre": "антиутопия", "evaluation": 4.0},
    {"book_id": 10, "title": "Крестный отец", "author": "Марио Пьюзо", "available": "В наличии", "genre": "роман", "evaluation": 4.9},
]

my_books = []

borrowed_books = []
#-------------------------------------------------------------------------------------------------------------------------------------

users = {
    "admin": "12345",
    "user": "qwerty"
}


def main_menu():
    while True:
        print("\nМеню:")
        print("1. Войти")
        print("2. Зарегистрироваться")
        print("3. Выйти")
        choice = input("Выбор: ")
        if choice == '1':
            username = login()
            if username:
                if username == "admin":
                    admin_menu()
                else:
                    user_menu(username)
            else:
                print("Неверный логин или пароль.")
        elif choice == '2':
            register()
        elif choice == '3':
            break
        else:
            print("Неверный выбор! Вводите числа от 1 до 3!")

def login():
    username = input("Логин: ")
    password = input("Пароль: ")
    return username if username in users and users[username] == password else None


def register():
    username = input("Введите желаемый логин: ")
    if username in users:
        print("Логин занят!")
        return None
    password = input("Введите пароль: ")
    confirm_password = input("Подтвердите пароль: ")
    if password != confirm_password:
        print("Пароли не совпадают!")
        return None
    users[username] = password
    print(f"Пользователь {username} успешно зарегистрирован.")
    return username        

def user_menu(username):
    while True:
        print("\nМеню пользователя:")
        print("1. Просмотреть книги")
        print("2. Найти книгу")
        print("3. Отсортировать по рейтингу")
        print("4. Занять книгу")
        print("5. История займов")
        print("6. Изменить логин/пароль")
        print("7. Выйти")
        choice = input("Выбор: ")

        if choice == '1':
            show_books()
        elif choice == '2':
            query = input("Введите название, автора или жанр книги: ")
            results = search_books(books, query)
            if results:
                print(f"\nРезультаты поиска по запросу: {query}")
                print(f"{'Название':<30} {'Автор':<20} {'Жанр'}")
                print("_" * 70)
                for book in results:
                    print(f"{book['title']:<30} {book['author']:<20} ({book['genre']})")
            else:
                print("Книги не найдены.")
        elif choice == '3':
            order = input("Введите '1' для сортировки по возрастанию или '2' для убывания: ")
            ascending = order.lower() == '1'
            sorted_books = sort_books(books, ascending)
            print(f"{'Название':<30} {'Автор':<20} {'Рейтинг'}")
            print("_" * 70)
            for book in sorted_books:
                print(f"{book['title']:<30} {book['author']:<20} {book['evaluation']}")
        elif choice == '4':
            show_books()
            book_id = int(input("Введите ID книги, которую хотите занять: "))
            borrow_book(username, book_id, my_books)
        elif choice == '5':
            show_borrowed_books(username, my_books)
        elif choice == '6':
            change_user_credentials(username)
        elif choice == '7':
            break
        else:
            print("Неверный выбор.")
#____________________________________________________
def admin_menu():
    while True:
        print("\nМеню администратора:")
        print("1. Добавить книгу")
        print("2. Удалить книгу")
        print("3. Просмотреть книги")
        print("4. Найти книгу")
        print("5. Изменить данные пользователя")
        print("6. Список отданных книг")
        print("7. Количество отданных книг")
        print("8. Отсортировать по рейтингу")
        print("9. Выйти")
        choice = input("Выбор: ")
        if choice == '1':
            add_book(books)
        elif choice == '2':
            delete_book()
        elif choice == '3':
            show_books()
        elif choice == '4':
            query = input("Введите название, автора или жанр книги: ")
            results = search_books(books, query)
            if results:
                print(f"\nРезультаты поиска по запросу: {query}")
                print(f"{'Название':<30} {'Автор':<20} {'Жанр'}")
                print("_" * 70)
                for book in results:
                    print(f"{book['title']:<30} {book['author']:<20} ({book['genre']})")
            else:
                print("Книги не найдены.")
        elif choice == '5':
            change_user_credentials()
        elif choice == '6':
            show_borrowed_books_table(borrowed_books)
        elif choice == '7':
            print(f"Общее количество отданных книг: {len(borrowed_books)}")
        elif choice == '8':
            order = input("Введите '1' для сортировки по возрастанию или '2' для убывания: ")
            ascending = order.lower() == '1'
            sorted_books = sort_books(books, ascending)
            print(f"{'Название':<30} {'Автор':<20} {'Рейтинг'}")
            print("_" * 70)
            for book in sorted_books:
                print(f"{book['title']:<30} {book['author']:<20} {book['evaluation']}")
        elif choice == '9':
            break
        else:
            print("Неверный выбор.")




#______________________________________________________________________________________________________________________________________________
#_________Действия с книгами_______________________________________________________________________________________________________________
def show_books():
    if not books:
        print("\nСписок книг пуст.")
        return
    
    print("\nСписок книг:")
    print(f"{'ID':<5} {'Название':<30} {'Автор':<25} {'Доступность':<15} {'Жанр':<15} {'Оценка':<3}")
    print("_" * 110)
    for book in books:
        print(f"{book['book_id']:<5} {book['title']:<30} {book['author']:<25} {book['available']:<15} {book['genre']:<15} {book['evaluation']:<3}")
    print("_" * 110)
#____________________________________________________________________________________

def add_book(books):
    """Adds a new book to the books list."""
    next_id = max(book['book_id'] for book in books) + 1 if books else 1
    title = input("Введите название книги: ")
    author = input("Введите автора книги: ")
    available = input("Введите статус наличия (В наличии/Нет в наличии): ")  
    genre = input("Введите жанр книги: ")
    evaluation = float(input("Введите оценку книги: "))

    new_book = {
        "book_id": next_id,
        "title": title,
        "author": author,
        "available": available,
        "genre": genre,
        "evaluation": evaluation
    }
    books.append(new_book)
    print("Книга добавлена!")
#___________________________________________________________________________________

def delete_book():
    show_books()
    try:
        book_id = int(input("Введите ID книги для удаления: "))
        book = next((book for book in books if book['book_id'] == book_id), None)
        if book:
            books.remove(book)
            print("Книга удалена.")
        else:
            print("Книга не найдена.")
    except ValueError:
        print("Некорректный ID книги.")
#______________________________________________________________________________________

def search_books(books, query):
    query = query.lower()
    return list(filter(lambda book: query in book['title'].lower() or query in book['author'].lower() or query in book['genre'].lower(), books))
#_______________________________________________________________________________________________________________

def sort_books(books, ascending=True):
    
    try:
        return sorted(books, key=lambda book: book['evaluation'], reverse=not ascending)
    except KeyError:
        print("Ошибка: Ключ 'evaluation' не найден в словаре книги.")
        return books 

#__________________________________________________________________________________

def borrow_book(username, book_id, borrowed_books):
    book = next((b for b in books if b["book_id"] == book_id), None)
    if book and book["available"] == "В наличии":
        borrowed_books.append({"username": username, "book_id": book_id})
        book["available"] = "Нет в наличии"
        print(f"Книга '{book['title']}' успешно добавлена в список взятых книг.")
    else:
        print("Эта книга недоступна для займа.")
#_____________________________________________________________________________

def show_borrowed_books(username, borrowed_books):
    user_books = [b for b in borrowed_books if b["username"] == username]
    if user_books:
        print("\nКниги, взятые вами:")
        print(f"{'ID':<5} {'Название':<30} {'Автор':<25} {'Жанр':<15} {'Оценка':<5}") 
        print("_" * 100) 
        for book_data in user_books:
            book = next((b for b in books if b["book_id"] == book_data["book_id"]), None)
            if book:
                print(f"{book['book_id']:<5} {book['title']:<30} {book['author']:<25} {book['genre']:<15} {book['evaluation']:<5}")
            else:
                print(f"Ошибка: книга с ID {book_data['book_id']} не найдена в списке книг.")
        print("_" * 100) 
    else:
        print("Вы еще не взяли ни одной книги.")

#________________________________________________________________________________________
def show_borrowed_books_table(borrowed_books):
    if not borrowed_books:
        print("Список отданных книг пуст.")
        return

    print("\nСписок отданных книг:")
    print(f"{'Пользователь':<15} {'ID книги':<10} {'Название книги'}")
    print("-" * 50)
    for entry in borrowed_books:
        book = next((b for b in books if b["book_id"] == entry["book_id"]), None)
        book_title = book["title"] if book else "Книга не найдена"
        print(f"{entry['username']:<15} {entry['book_id']:<10} {book_title}")
#_______________________________________________________________________________________
def change_user_credentials(username):
    if username not in users:
        print("Пользователь не найден.")
        return

    print(f"\nИзменение данных пользователя {username}:")
    new_login = input("Новый логин (оставьте пустым, чтобы не менять): ")
    new_password = input("Новый пароль (оставьте пустым, чтобы не менять): ")
    confirm_password = ""
    if new_password:
        confirm_password = input("Подтвердите новый пароль: ")

    if new_password and new_password != confirm_password:
        print("Пароли не совпадают!")
        return

    if new_login:
        users[new_login] = users.pop(username) 
        username = new_login 
    if new_password:
        users[username] = new_password

    print(f"Данные пользователя {username} успешно изменены.")


if __name__ == "__main__":
    print("Добро пожаловать в библиотеку Книгоград (не Читайгород)")
    main_menu()