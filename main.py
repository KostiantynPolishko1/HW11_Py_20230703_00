
def arr_word_num(txt):
    print(txt)
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

    print()
    for i in resTxt:
        print(i)

#======================main=============================#

txt_in = "-12.3-35=40, 50*10+30/40 Hello, " \
         ":!.word2023!0.23/cup:?- How\nis\tgoing your deals?" \
         " Are you ready.for New Summer 2024."

# function in order to divide phrases complexity on the words and numbers
arr_word_num(txt_in)