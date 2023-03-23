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


def input_line():
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

