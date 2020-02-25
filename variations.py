#!/usr/bin/env python3.7

message = input("Enter a message: ")
print(f"Lowercase: {message.lower()}")
print(f"Uppercase: {message.upper()}")
print(f"Capitalized: {message.capitalize()}")
print(f"Title Case: {message.title()}")
#print("Words: {message.split()}")
words = message.split()
print("Words: ", words)
sorted_words = sorted(words)
print(f"Alphabetic First Word: {sorted_words[0]}")
print(f"Alphabetic Last Word: {sorted_words[-1]}")
