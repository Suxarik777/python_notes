from func_for_file import read_file, recording_file
from print_message_console import print_menu
from inputs import input_menu_item

notes_data_array = read_file()
menu_item = 0
uncorrected = True

while True:
    if menu_item == 8: break
    else:
        print_menu()
        menu_item = input_menu_item()