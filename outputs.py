from func_for_file import read_file
from inputs import input_submenu_outputs, input_number_note


def output_note():
    data_list = read_file()

    # выбираем пункт меню
    text = "Что вы хотите посмотреть?" \
           "\n1 - Все заметки" \
           "\n2 - Заметку по номеру" \
           "\n3 - Выборку заметок по дате"
    print(text)

    submenu_item = input_submenu_outputs() #проверка ввода в inputs

    if submenu_item == 1:
        show_all: str = ''
        for i in range(len(data_list)):
            row = ' '.join(data_list[i])
            show_all += row + '\n'
        print(show_all)

    if submenu_item == 2:
        text = 'Введите номер интересующей заметки'
        print(text)

        index_row = input_number_note() #проверка ввода в inputs

        show_row = ' '.join(data_list[index_row])
        print(show_row)

    if submenu_item == 3:

