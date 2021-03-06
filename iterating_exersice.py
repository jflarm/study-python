#!/usr/bin/python3.7
# Este lo hizo el instructor del curso de LinuxAcademy
# El usa la variable prefix para ir concatenando el numero de linea y los \
# demas datos requeridos en el ejercicio

# Building on top of the conditional exercise, write a script that will loop \
# through a list of users where each item is a user dictionary from the previous \
# exercise printing out each user’s status on a separate line. Additionally, \
# print the line number at the beginning of each line, starting with line 1. Be \
# sure to include a variety of user configurations in the users list.
# User Keys:
#     'admin' - a boolean representing whether the user is an admin user.
#     'active' - a boolean representing whether the user is currently active.
#     'name' - a string that is the user’s name.
# Depending on the values of the user, print one of the following to the screen \
# when you run the script.
#     Print (ADMIN) followed by the user’s name if the user is an admin.
#     Print ACTIVE - followed by the user’s name if the user is active.
#     Print ACTIVE - (ADMIN) followed by the user’s name if the user is an admin \
#     and active.
#     Print the user’s name if neither active nor an admin.

users = [
    { 'admin': True, 'active': True, 'name': 'Kevin' },
    { 'admin': True, 'active': False, 'name': 'Elisabeth' },
    { 'admin': False, 'active': True, 'name': 'Josh' },
    { 'admin': False, 'active': False, 'name': 'Kim' },
]

line = 1

for user in users:
    prefix = f"{line} "

    if user['admin'] and user['active']:
        prefix += "ACTIVE - (ADMIN) "
    elif user['admin']:
        prefix += "(ADMIN) - "
    elif user['active']:
        prefix += "ACTIVE - "

    print(prefix + user['name'])
    line += 1