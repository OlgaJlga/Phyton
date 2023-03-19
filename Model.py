import json
from os import system
import time
import View
def read():
    try:
        with open('Book.json', 'r', encoding="utf-8") as data:
            book = json.loads(data.read())
        return book
    except:
        return []
def save(book):
    with open('Book.json', 'w', encoding="utf-8") as data:
        json.dump(book, data, indent=4, ensure_ascii=False)
def create_contact(book):
    Famyli = input("Введите фамилию: ")
    firstname = input("Введите имя: ")
    patronymic = input("Введите отчество: ")
    Telefon = input("Введите телефон: ")
    contact = {"Famyli": Famyli, "Firstname": firstname,
               "Patronymic": patronymic, "Telefon": Telefon}
    book.append(contact)
    book = sort(book)
    save(book)
    print('Контакт создан')
    return book
def del_contact(book):
    print("Введите номер контакта для удаления: ")
    time.sleep(1)
    View.view(book)
    num_contact = input('Введите номер контакта для удаления: ')
    if num_contact.isdigit() and int(num_contact) <= len(book):
        book.pop(int(num_contact)-1)
        save(book)
        print('Контакт удален')
    else:
        print("Неверно введен номер контакта")        
    return book
def sort(book):
    lst = []
    book_sort = []
    for note in book:
        lst.append([note['Famyli'], note['Firstname'],
                   note["Patronymic"], note["Telefon"]])
    lst.sort()
    for note in lst:
        book_sort.append(
            {"Famyli": note[0], "Firstname": note[1], "Patronymic": note[2], "Telefon": note[3]})
    return book_sort