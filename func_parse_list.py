#!/usr/bin/env python3.7

def parse_list(lista):
    """
    parse_list(a) parses a list, creating three lists: strings, numbers and lists
    """
    numlist = []
    strlist = []
    listlist = []
    for i in lista:
        if isinstance(i, int) or isinstance(i, float):
            numlist.append(i)
        elif isinstance(i, str):
            strlist.append(i)
        elif isinstance(i, list):
            listlist.append(i)
        else:
            pass
    return strlist, numlist, listlist

# origlist = ['apple', 'phone', 'words']
# mylist = ['Mic', 'Phone', 323.12, 3123.123, 'Justin', 'Bag', 'Cliff Bars', 134, '321', 99, 42.55, ['apple', 'phone', 'words']]
# print(parse_list(mylist))