from os import system
from msvcrt import getwch
import time
def menu():
    time.sleep(1)
    system('CLS') 
    move = {1: 'Создать контакт', 2: 'Прочитать книгу', 3:'Удалить контакт', 4: 'Выход'}
    print('Выберите операцию', move)
    n = getwch() 
    if n.isdigit() and n in '1234':
        system('CLS')
        return int(n)
    else:
        system('CLS')
        print('Введите из предложенных вариантов')
def view(book):
    print('Список контактов телефонного справочника: ')
    table = [['Фамилия', 'Имя', 'Отчество', 'Номер телефона']]
    for contact in book:
        contact = list(contact.values())
        table.append(contact)
    for ind, item in enumerate(table):
        if ind == 0:
            ind = '№'
        print(ind, ' ', *map(lambda x: str(x) + ' ' * (20 - len(x)), item))
def view2(book):
    key = 0
    if book == []:
        return
    table = [['Фамилия', 'Имя', 'Отчество', 'Номер телефона']]
    for contact in book:
        contact = list(contact.values())
        table.append(contact)
    while True:
        system('CLS')
        print('Список контактов телефонного справочника: ')
        size = (len(table) + 3) // 4
        print(f'[{key + 1}/{size}]')
        print('№', ' ', *map(lambda x: str(x) +
              ' ' * (20 - len(x)), table[0]))
        for ind, item in enumerate(table[key*5 + 1: key*5 + 2]):
            print(key*5 + ind + 1, ' ', *
                  map(lambda x: str(x) + ' ' * (20 - len(x)), item))
        print('Нажмите для просмотра a или d, для выхода в меню - q')
        key_ch = getwch()
        if key_ch in 'd' and key < size - 1:
            key += 1
        if key_ch in 'a' and key > 0:
            key -= 1
        if key_ch in 'q':
            break