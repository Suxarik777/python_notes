from func_for_file import read_file, recording_file
from print_message_console import print_menu
from inputs import input_menu_item, input_note
from outputs import output_note
from edit import edit_row_note


menu_item = 0
uncorrected = True

while True:
    if menu_item == 8: break
    else:
        print_menu()
        menu_item = input_menu_item()
        if menu_item == 1:
            input_note()
        if menu_item == 2:
            output_note()
        if menu_item == 3:
            edit_row_note()