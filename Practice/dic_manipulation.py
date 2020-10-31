#!/usr/bin/python3
import json

dictionary = {}
_list = ["Andrew", "John", "Pam", "Gissele"]

id = 0
for i in _list:
    id += 1
    dictionary[i] = id

print(dictionary)
