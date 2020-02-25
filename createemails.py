#!/usr/bin/env python3.7

# This script will create emails from a list of names

nombres = ['James Butt', 'Josephine Darakjy', 'Art Venere', 'Lenna Paprocki', 'Donette Foller', 'Simona Morasca', 'Mitsue Tollner', 'Leota Dilliard', 'Sage Wieser']
emails = []
direcciones = {}
for i in nombres:
    first_name = i.split(' ',1)[0]
    last_name = i.split(' ',1)[1]
    if len(first_name) > 6:
        first_name = first_name[0:3]
    email = f"{first_name.lower()}.{last_name.lower()}@yahoo.com" 
    emails.append(email)
    direcciones[i] = email
print(nombres)
print('\n')
print(emails)
print('\n')
print(direcciones)
