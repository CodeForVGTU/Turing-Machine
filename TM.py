from consolemenu import ConsoleMenu  # https://console-menu.readthedocs.io/en/latest/
from consolemenu.items import SubmenuItem, FunctionItem
import concurrent.futures
import keyboard
import os
from colorama import Back
from collections import defaultdict

all_results = ""


def tm_menu():
    menu = ConsoleMenu("Turing Machine Simulator", "Created with Python")

    submenu = ConsoleMenu("About Us")
    submenu.prologue_text = "This is Turing Machine Simulator created by Vilnius Gediminas Technical University " \
                            "PRIfs 18/6 student - Rimvydas Kanapka." \
                            " This program is created for Architecture of Computers and Computer Networks."

    menu.append_item(FunctionItem("RUN Turing Machine", action))  # First menu item
    menu.append_item(SubmenuItem("About Us", submenu, menu=menu))  # Second menu item
    menu.show()


def action():  # must be named action to call it in console menu api
    global all_results
    all_results = ""
    all_files = []
    file = "do not stop"

    print("Enter {Q} if you wrote all your file names.\n"
          "After writing {Q}, if you want to Stop, click Q.")

    while file != "Q":

        file = input("Enter file name: ")

        if os.path.isfile(file): # cheking if file exists
            all_files.append(file)
            print(Back.GREEN + "File added." + Back.BLACK)
        elif file == "Q":
            continue
        else:
            print(Back.RED + "File doesn't exist. Try other name." + Back.BLACK)

    print(Back.GREEN + "Your file names: " + str(all_files) + Back.BLACK)

    print("PRESS ENTER TO RUN TURING MACHINE")
    keyboard.wait('enter')

    def turing_machine(file_name):
        global all_results

        with open(file_name) as f:
            # avoiding calling line.strip() twice, using a generator
            # https://stackoverflow.com/questions/4842057/easiest-way-to-ignore-blank-lines-when-reading-a-file-in-python
            lines = [l for l in (line.strip() for line in f) if l]  # tape code is added to list
        f.close()

        head_position = int(lines[0]) - 1  # place from where head starts moving | minus -, because list starts from 0
        tape = list(lines[1])  # starting tape value
        del lines[:2]  # deleting first two elements of list - head start position & tape value
        dictionary = defaultdict(list)

        for key in lines:
            code = key.split(" ", 4)  # dividing string 4 times by space
            current_state = code[0]
            current_symbol = code[1]
            next_symbol = code[2]
            right_left = code[3]
            next_state = code[4]
            sublist = [next_symbol, right_left, next_state]  # needed value
            dictionary[(current_state, current_symbol)].append(sublist)  # Everything is added to dict

        status = '0'  # first state always is 0
        while True:
            try:
                symbol = tape[head_position]
                tape[head_position] = dictionary[status, symbol][0][0]

                if tape[head_position] != symbol: # if it's same line - it won't be printed
                    print(''.join(tape))

                if dictionary[status, symbol][0][1] == 'R':
                    head_position += 1
                    if head_position > len(''.join(tape)): # out of range: RIGHT - Index error
                        print(file_name + " Halted")
                        break
                else:
                    head_position -= 1
                    if head_position < 0: # out of range: LEFT - Index error
                        print(file_name + " Halted")
                        break

                status = dictionary[status, symbol][0][2]
 
                if keyboard.is_pressed('q'):
                    print(file_name + " Stopped")
                    break

            except IndexError:
                print(file_name + " Halted")  # Index error
                break

        all_results += file_name + ' - ' + ''.join(tape) + "\n"

    with concurrent.futures.ThreadPoolExecutor() as executor: # multiple thread executor
        results = executor.map(turing_machine, all_files)

        for result in results:
            if result is not None:
                print(result)

    print(Back.GREEN + "Results:\n" + Back.BLACK + all_results)
    print("PRESS ENTER TO GO BACK TO MENU")
    keyboard.wait('enter')


tm_menu()
