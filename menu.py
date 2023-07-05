import os
import time

def clean_s() -> None:
    time.sleep(0)
    os.system('CLS')

def exit_menu():
    while True:
        out_submenu = input("\texit ")
        if not out_submenu:
            os.system('CLS')
            return 1
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

#=========FUNCTION TO SPLIT ON SEPARATELY WORDS & NUMBERS=========#

def arr_word_num(txt):
    # print(txt)
    symbols2 = "!?.,:;+-*/"
    resAlpha: str = ''
    resNumer: str = ''
    resTxt = []
    for i in range(len(txt)):
        if txt[i].isalpha():
            resAlpha += txt[i]
        else:
            if resAlpha != '':
                resTxt.append(resAlpha)
                resAlpha = ''
            else:
                continue
    resTxt.append(resAlpha)

    for i in range(len(txt)):
        if txt[i].isnumeric():
            resNumer += txt[i]
        elif not txt[i].isnumeric() and txt[i] == '.':
            resNumer += txt[i]
        else:
            if resNumer != '':
                resTxt.append(resNumer)
                resNumer = ''
            else:
                continue
    resTxt.append(resNumer)

    for i in symbols2:
        resTxt[:] = [x for x in resTxt if x != i]
    resTxt[:] = [x for x in resTxt if x != '']

    # delete the symbols in the start and in the end
    suffix = ('!', '?', ',', '.', ':', ';', '+', '-', '*', '/')

    for i in range(len(resTxt)):
        if not resTxt[i].isalpha() and not resTxt[i].isnumeric():
            if resTxt[i].startswith(suffix) or resTxt[i].endswith(suffix):
                while True:
                    if resTxt[i].startswith(suffix):
                        resTxt[i] = resTxt[i][1:]
                        continue
                    elif resTxt[i].endswith(suffix):
                        resTxt[i] = resTxt[i][:len(resTxt[i]) - 1]
                        continue
                    break

    # print()
    # for i in resTxt:
    #     print(i)

    return resTxt

#===================MENU SECTION REPORT===========================#

def func_1(ind_m, ind_s, menu_s, txt: str, logic: bool = ''): #Num symbols
    ind_s = 0 if logic else ind_s
    print("\n{}.{} {}".format(ind_m + 1, ind_s + 1, menu_s[ind_s][0]))

    num_sym = len(txt)
    print("\tQty of symbols -> ", num_sym if num_sym else "NO TEXT!")

    return 0 if logic else exit_menu()

def func_2(ind_m, ind_s, menu_s, txt: str, logic: bool = ''): #Num digits
    ind_s = 1 if logic else ind_s
    print("\n{}.{} {}".format(ind_m + 1, ind_s + 1, menu_s[ind_s][0]))

    num_digit = 0
    for i in txt:
        if i.isdigit():
            num_digit += 1

    num_sym = len(txt)
    print("\tQty of digits -> ", num_digit if num_sym else "NO TEXT!")

    return 0 if logic else exit_menu()

def func_3(ind_m, ind_s, menu_s, txt: str, logic: bool = ''): #Num letters
    ind_s = 2 if logic else ind_s
    print("\n{}.{} {}".format(ind_m + 1, ind_s + 1, menu_s[ind_s][0]))

    num_letter = 0
    for i in txt:
        if i.isdigit():
            num_letter += 1

    num_sym = len(txt)
    print("\tQty of letters -> ", num_letter if num_sym else "NO TEXT!")

    return 0 if logic else exit_menu()

def func_4(ind_m, ind_s, menu_s, txt: str, logic: bool = ''): #Num Up letters
    ind_s = 3 if logic else ind_s
    print("\n{}.{} {}".format(ind_m + 1, ind_s + 1, menu_s[ind_s][0]))

    num_up_letter = 0
    for i in txt:
        if i.isupper():
            num_up_letter += 1

    num_sym = len(txt)
    print("\tQty of Up letters -> ", num_up_letter if num_sym else "NO TEXT!")

    return 0 if logic else exit_menu()

def func_5(ind_m, ind_s, menu_s, txt: str, logic: bool = ''): #Num Low letters
    ind_s = 4 if logic else ind_s
    print("\n{}.{} {}".format(ind_m + 1, ind_s + 1, menu_s[ind_s][0]))

    num_low_letter = 0
    for i in txt:
        if i.islower():
            num_low_letter += 1

    num_sym = len(txt)
    print("\tQty of Low letters -> ", num_low_letter if num_sym else "NO TEXT!")

    return 0 if logic else exit_menu()

def func_6(ind_m, ind_s, menu_s, txt: str, logic: bool = ''): #Num spaces
    ind_s = 5 if logic else ind_s
    print("\n{}.{} {}".format(ind_m + 1, ind_s + 1, menu_s[ind_s][0]))

    num_space = txt.count(' ')

    num_sym = len(txt)
    print("\tQty of spaces -> ", num_space if num_sym else "NO TEXT!")

    return 0 if logic else exit_menu()

def func_7(ind_m, ind_s, menu_s, txt_in: str, logic: bool = ''): #Num numbers
    ind_s = 6 if logic else ind_s
    print("\n{}.{} {}".format(ind_m + 1, ind_s + 1, menu_s[ind_s][0]))

    arr_wn = arr_word_num(txt_in)
    arr_num = []
    num_numbers = 0

    for i in arr_wn:
        if not i.isalpha() and i.find('.') != -1:
            arr_num.append(i)
            num_numbers += 1
        elif i.isnumeric():
            arr_num.append(i)
            num_numbers += 1

    print("Numbers\t-> ", arr_num)
    num_sym = len(txt_in)
    print(" Qty of numbers -> ", num_numbers if num_sym else "NO TEXT!")

    return 0 if logic else exit_menu()

def func_8(ind_m, ind_s, menu_s, txt_in: str, logic: bool = ''): #Num words
    ind_s = 7 if logic else ind_s
    print("\n{}.{} {}".format(ind_m + 1, ind_s + 1, menu_s[ind_s][0]))
    if not len(txt_in):
        print("NO TEXT")
        exit_menu()

    arr_wn = arr_word_num(txt_in)
    sentence = ' '.join(arr_wn)

    for i in arr_wn:
        if i.isalpha():
            print(i, "\t= ", sentence.count(i), " p.c.")

    return 0 if logic else exit_menu()

def func_9(ind_m, ind_s, menu_s, txt: str): #Total report
    print("\n{}.{} {}".format(ind_m + 1, ind_s + 1, menu_s[ind_s][0]))
    for i in range(len(menu_s)-2):
        menu_s[i][1](1, ind_s, menu_s, txt, True)
    exit_menu()

def func_10(ind_m, ind_s, menu_s, txt=None):
    print("\n{}.{} {}".format(ind_m + 1, ind_s + 1, menu_s[ind_s][0]))
    return True

#======================MENU FUNCTION=============================#

def input_txt(ind, menu, txt=None):
    print("\n {}. {}:".format(ind + 1, menu[ind][0]))
    str_txt = input("\t-> ")
    # str_txt = "-12.3-35=40, 50*10+30/40 Hello, " \
    #      ":!.word2023!0.23/cup:?- How\nis\tgoing your deals?" \
    #      " Are you ready.for New Summer 2024."

    if exit_menu():
        return str_txt

def report_txt(ind, menu, txt):
    ind_sub = 0
    menu_sub = {
        0: ["Num symbols", func_1],
        1: ["Num digits", func_2],
        2: ["Num letters", func_3],
        3: ["Num Up letters", func_4],
        4: ["Num Low letters", func_5],
        5: ["Num spaces", func_6],
        6: ["Num numbers", func_7],
        7: ["Num words", func_8],
        8: ["Total info", func_9],
        9: ["Exit", func_10]
    }

    while True:
        print("\n {}. {}:".format(ind+1, menu[ind][0]))
        print_menu(ind_sub, menu_sub, "report", ind)
        print(" \"w\" - Down, \"s\" - Up: -> ", end='')
        ind_sub, sub_operation = receive_pos(ind_sub, "report")
        clean_s()

        if not sub_operation:
            temp_value = menu_sub[ind_sub][1](ind, ind_sub, menu_sub, txt)
            if type(temp_value) == bool and temp_value:
                break

def modify_txt(ind, menu, txt_in):

    symbol_dict = {}
    symbol_new, symbol_old = '', ''
    while True:
        print("\n {}. {}:".format(ind + 1, menu[ind][0]))
        print("Text:\n\t", txt_in)

        print("List:")
        for i in symbol_dict:
            print("\told: \'{}\' -> new: \'{}\'".format(i, symbol_dict[i]))

        print("Fill symbols:")
        symbol_old = input("\told -> ")
        symbol_new = input("\tnew -> ")
        symbol_dict[symbol_old] = symbol_new

        out_submenu = input("\tcontinue ")
        if not out_submenu:
            os.system('CLS')
            continue
        else:
            break

    print("Replaced:")
    for i in symbol_dict:
        print("\told: \'{}\' -> new: \'{}\'".format(i, symbol_dict[i]))
        txt_in = txt_in.replace(i, symbol_dict[i])

    print("Result:\n\t-> ", txt_in)

    exit_menu()

def exit_txt(ind, menu, txt=None):
    print("\n {}. {}".format(ind+1, menu[ind][0]))
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
        tempValue = menu_f[ind_menu][1](ind_menu, menu_f, strTxt)
        if type(tempValue) == str:
            strTxt = tempValue
        elif type(tempValue) == bool and tempValue:
            break
