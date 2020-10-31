#!/usr/bin/python3

def convert_to_list(string):
    return list(string.split(" "))

d_flag = input("Are these main files?\n1) yes (type '1')\n2) no (type '2')\n")

type_file = input("Choose a file extension:\n1) .c (type '1')\n2) .py (type '2')\n")

if type_file == '1':
    extension = ".c"
elif type_file == '2':
    extension = ".py"

if d_flag == '1':
    nb_files = input("Enter number of files to create: ")
    nb_files = int(nb_files)
    for i in range(nb_files + 1):
        filename = str(i) + "-main" + str(extension)
        with open(filename, mode="w", encoding="utf-8") as fd:
            fd.write("")

elif d_flag == '2':
    names = input("Enter names of files separated by space please:\n")
    names = str(names)
    ls = convert_to_list(names)
    for i in range(len(ls)):
        with open(ls[i], mode="w", encoding="utf-8") as fd:
            if type_file == "2":
                fd.write("#!/usr/bin/python3")
            elif type_file == "1":
                fd.write("#include <stdlib.h>\n#include <stdio.h>\n\n/**\n *\n */\n")
            fd.write("")

else:
    print("Something wento wrong :(. You probably didnt enter the numbers properly.")
