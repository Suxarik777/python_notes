from datetime import date

from func_for_file import read_file, recording_file


def input_menu_item() -> int:
    MENU_ITEMS = 4
    menu_item_string = input('Введите пункт меню:\n')
    if menu_item_string.isdigit():
        menu_item = int(menu_item_string)
        if 0 < menu_item <= MENU_ITEMS or menu_item == 8:
            return int(menu_item)
        else:
            print("УПС! Что-то не так :(\nЧисло некорректно\n")
            input_menu_item()
    else:
        print("УПС! Что-то не так :(\nВведите числа, указанные напротив пунктов меню\n")
        input_menu_item()

def input_submenu() -> int:
    MENU_ITEMS = 3
    menu_item_string = input('Введите пункт меню:\n')
    if menu_item_string.isdigit():
        menu_item = int(menu_item_string)
        if 0 < menu_item <= MENU_ITEMS:
            return int(menu_item)
        else:
            print("УПС! Что-то не так :(\nЧисло некорректно\n")
            input_submenu()
    else:
        print("УПС! Что-то не так :(\nВведите числа, указанные напротив пунктов меню\n")
        input_submenu()


def input_note():
    data_list = read_file()
    user_input = input("Пишите заметку: ")
    data_sublist = [user_input]

    # добавляем дату
    day = date.today()
    day_str = day.strftime('%d-%m-%Y')
    data_sublist.insert(0, day_str)

    # добавляем порядковый номер строки
    new_number_element = str(len(data_list))
    data_sublist.insert(0, new_number_element)

    data_list.append(data_sublist)
    recording_file(data_list)

def input_number_note() -> int:
    data_notes = read_file()
    len_list_data = len(data_notes)
    number_note = input('Введите номер заметки:')
    if number_note.isdigit():
        number = int(number_note)
        if 0 <= number < len_list_data:
            return int(number)
        else:
            print("УПС! Что-то не так :(\nВидимо такой записи нет\n")
            input_number_note()
    else:
        print("УПС! Что-то не так :(\nВведите числа, буковки и символы не подходят\n")
        input_number_note()

def input_user_filter_date():
    CHECK_CORRECT_LEN_STR = 21 #'DD-MM-YYYY DD-MM-YYYY'
    date = input()

    check_digit = "".join(c for c in date if c.isdecimal()) # убираем все символы, кроме чисел

    if len(date) == CHECK_CORRECT_LEN_STR and check_digit.isdigit():
        date_list = date.split() #['22-22-2222', '22-22-2222']
        return date_list
    else:
        print("УПС! Кажется вы ввели не корректные данные"
              "\nПопробуйте в следующий раз")


