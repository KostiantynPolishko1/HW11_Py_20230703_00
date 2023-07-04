import os
import time

def clean_s() -> None:
    time.sleep(0)
    os.system('CLS')

def exit_menu():
    while True:
        out_submenu = input("\texit -> ")
        if not out_submenu:
            os.system('CLS')
            return True
        else:
            print("ERROR!")
            continue

def print_menu(ind_pos, arr, name_f="", ind_menu: int=""):
    print("\nMenu:") if name_f == '' else None
    for i in range(len(arr)):
        if i == ind_pos:
            print("-> {}{} {}".format((str(ind_menu + 1) + '.') if name_f == "report" else '', str(i+1) + '.', arr[i][0]))
            continue
        print("   {}{} {}".format((str(ind_menu + 1) + '.') if name_f == "report" else '', str(i+1) + '.', arr[i][0]))

def receive_pos(ind_pos=0, name_f = ""):
    min_ind, max_ind = 0, 3
    if name_f == "report":
        max_ind = 9

    while True:
        direct = input(" ")

        # increment & decrement
        if not direct:
            return ind_pos, direct
        elif direct == 'W' or direct == 'w':
            ind_pos += 1
        elif direct == 'S' or direct == 's':
            ind_pos -= 1
        else:
            print("ERROR!")
            print(" \"w\" - Down, \"s\" - Up: ->", end='')
            continue

        # check position
        if ind_pos < min_ind:
            ind_pos = max_ind
        elif ind_pos > max_ind:
            ind_pos = min_ind

        return ind_pos, direct

#===================MENU SECTION REPORT===========================#

def func_1(ind_m, ind_s, menu_s, txt: str): #Num symbols
    print("{}.{} {}".format(ind_m + 1, ind_s + 1, menu_s[ind_s][0]))
    if exit_menu():
        return 0

def func_2(ind_m, ind_s, menu_s, txt: str): #Num digits
    print("{}.{} {}".format(ind_m + 1, ind_s + 1, menu_s[ind_s][0]))
    if exit_menu():
        return 0

def func_3(ind_m, ind_s, menu_s, txt: str): #Num numbers
    print("{}.{} {}".format(ind_m + 1, ind_s + 1, menu_s[ind_s][0]))
    if exit_menu():
        return 0

def func_4(ind_m, ind_s, menu_s, txt: str): #Num letters
    print("{}.{} {}".format(ind_m + 1, ind_s + 1, menu_s[ind_s][0]))
    if exit_menu():
        return 0

def func_5(ind_m, ind_s, menu_s, txt: str): #Num Up letters
    print("{}.{} {}".format(ind_m + 1, ind_s + 1, menu_s[ind_s][0]))
    if exit_menu():
        return 0

def func_6(ind_m, ind_s, menu_s, txt: str): #Num Low letters
    print("{}.{} {}".format(ind_m + 1, ind_s + 1, menu_s[ind_s][0]))
    if exit_menu():
        return 0

def func_7(ind_m, ind_s, menu_s, txt: str): #Num spaces
    print("{}.{} {}".format(ind_m + 1, ind_s + 1, menu_s[ind_s][0]))
    if exit_menu():
        return 0

def func_8(ind_m, ind_s, menu_s, txt: str): #Num words, numbers
    print("{}.{} {}".format(ind_m + 1, ind_s + 1, menu_s[ind_s][0]))
    if exit_menu():
        return 0

def func_9(ind_m, ind_s, menu_s, txt: str): #Total report
    print("{}.{} {}".format(ind_m + 1, ind_s + 1, menu_s[ind_s][0]))
    if exit_menu():
        return 0

def func_10(ind_m, ind_s, menu_s, txt=None):
    print("{}.{} {}".format(ind_m + 1, ind_s + 1, menu_s[ind_s][0]))
    return True

#======================MENU FUNCTION=============================#

def input_txt(ind, txt=None):
    print("\n {}. Input:".format(ind + 1))
    str_txt = input("\t-> ")
    # str_txt = "-12.3-35=40, 50*10+30/40 Hello, " \
    #      ":!.word2023!0.23/cup:?- How\nis\tgoing your deals?" \
    #      " Are you ready.for New Summer 2024."

    if exit_menu():
        return str_txt

def report_txt(ind, txt):
    ind_sub = 0
    menu_sub = {
        0: ["Num symbols", func_1],
        1: ["Num digits", func_2],
        2: ["Num numbers", func_3],
        3: ["Num letters", func_4],
        4: ["Num Up letters", func_5],
        5: ["Num Low letters", func_6],
        6: ["Num spaces", func_7],
        7: ["Num words, numbers", func_8],
        8: ["Total info", func_9],
        9: ["Exit", func_10]
    }

    while True:
        print("\n {}. Reports:".format(ind+1))
        print_menu(ind_sub, menu_sub, "report", ind)
        print(" \"w\" - Down, \"s\" - Up: -> ", end='')
        ind_sub, sub_operation = receive_pos(ind_sub, "report")
        clean_s()

        if not sub_operation:
            temp_value = menu_sub[ind_sub][1](ind, ind_sub, menu_sub, txt)
            if type(temp_value) == bool and temp_value:
                break

def modify_txt(ind, txt):
    print("\n {}. Modify:".format(ind+1))

def exit_txt(ind, txt=None):
    print("\n {}. Exit".format(ind+1))
    return True

#======================main=============================#

ind_menu = 0
strTxt: str = ''

menu_f = {
    0: ["Input", input_txt],
    1: ["Report", report_txt],
    2: ["Modify", modify_txt],
    3: ["Exit", exit_txt]
}

while True:
    print_menu(ind_menu, menu_f)
    print(" \"w\" - Down, \"s\" - Up: ->", end='')
    ind_menu, operation = receive_pos(ind_menu)
    clean_s()

    if not operation:
        tempValue = menu_f[ind_menu][1](ind_menu, strTxt)
        if type(tempValue) == str:
            strTxt = tempValue
        elif type(tempValue) == bool and tempValue:
            break
