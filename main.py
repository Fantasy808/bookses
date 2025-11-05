try:
    myfile = open('hello.txt', 'r', encoding='utf-8')
    myfile.close()
except FileNotFoundError:
    myfile = open('hello.txt', 'w', encoding='utf-8')
    myfile.close()

books = []

def add_book():
    tittle_book = input('Введите название книги и год: ')
    myfile = open('hello.txt', 'a', encoding='utf-8')
    myfile.write(tittle_book + '\n')
    myfile.close()

def look_book():
    myfile = open('hello.txt', 'r', encoding='utf-8')
    books2 = myfile.read()
    myfile.close()
    print(books2)

def delete_book():
    title = input('Введите название книги которую хотите удалить: ')
    myfile = open('hello.txt', 'r', encoding='utf-8')
    books = myfile.readlines()
    myfile.close()

    new_books = []
    found = False
    for book in books:
        if title in book:
            found = True

        else:
            new_books.append(book)

    myfile = open('hello.txt', 'w', encoding='utf-8')
    myfile.writelines(new_books)
    myfile.close()
    myfile = open('hello.txt', 'r', encoding='utf-8')
    books2 = myfile.read()
    myfile.close()
    print(books2)

def search_book():
    search = input('Введите название книги или её номер для поиска: ')
    myfile = open('hello.txt', 'r', encoding='utf-8')
    books = myfile.readlines()
    myfile.close()

    for i, book in enumerate(books, 1):
        if search in book or search == str(i):
            print(book.strip())
        else:
            print('Книга не найдена')

def replaceable():
    myfile = open('hello.txt', 'r', encoding='utf-8')
    books = myfile.readlines()
    myfile.close()
    replaceable = input('Введите название заменяемой книги: ')
    replaceable2 = input('Введите название книги на которую вы замените: ')
    for i, book in enumerate(books, 1):
        if replaceable in book or replaceable == str(i):
            index = books.index(book)
            books[index] = replaceable2
    myfile = open('hello.txt', 'w', encoding='utf-8')
    myfile.writelines(books)
    myfile.close()

while True:
    print('1.Добавить книгу\n2.Просмотреть книги\n3.Удалить книгу по названию\n4.Найти книгу\n5.Перезапись')
    choise = int(input())
    if choise == 1:
        add_book()
    elif choise == 2:
        look_book()
    elif choise == 3:
        delete_book()
    elif choise == 4:
        search_book()
    elif choise == 5:
        replaceable()