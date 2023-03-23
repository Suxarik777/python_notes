from inputs import input_number_note, input_submenu
from func_for_file import read_file, recording_file

def edit_row_note():
    data_array = read_file()

    text = 'Введите номер интересующей заметки'
    print(text)

    index_row = input_number_note()  # проверка ввода в inputs

    row_text = f"Вы выбрали заметку: \n{' '.join(data_array[index_row])}"
    print(row_text + "\n")

    text_1 = 'Что делаем?' \
           '\n1 - Редактируем' \
           '\n2 - Выбираем другую' \
           '\n3 - Ничего не делаем'
    print(text_1)

    submenu_item = input_submenu() #проверка ввода числа меню

    if submenu_item == 1:
        data_array[index_row][2] = input("Введите новый текст в заметку:\n")
        recording_file(data_array)
        print("Данные записаны")

    if submenu_item == 2:
        edit_row_note()

    if submenu_item == 3:
        print('Ok ;)')
