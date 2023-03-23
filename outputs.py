from func_for_file import read_file
from inputs import input_submenu_outputs, input_number_note, input_user_filter_date


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
        text = 'Введите даты от и до в формате ДД-ММ-ГГГГ' \
               '\nпример: 12-12-2022 01-01-2023'
        print(text)
        user_filter_date = input_user_filter_date() #['22-22-2222', '22-22-2222']

        start_date = user_filter_date[0]
        end_date = user_filter_date[1]

        #убираем символ - из переменных
        start_date_digit = start_date.replace("-", "")
        end_date_digit = end_date.replace("-", "")

        start_date_int = int(start_date_digit)
        end_date_int = int(end_date_digit)

        show_row_filter: str = ''

        for i in range(len(data_list)):
            # убираем все символы, кроме чисел в 1 индексе sublist + переводим в int
            check_date_digit = int("".join(c for c in data_list[i][1] if c.isdecimal()))

            if start_date_int <= check_date_digit <= end_date_int:
                row = ' '.join(data_list[i])
                show_row_filter += row + '\n'

        if len(show_row_filter) > 0:
            print(show_row_filter)
        else:
            print("По заданным параметрам ничего не найдено!")

