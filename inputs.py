
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