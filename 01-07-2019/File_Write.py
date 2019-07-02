import os

try:
    f = open("new.txt", "w")
except FileNotFoundError:
    print("No File Found")

os.remove("new.txt")

try:
    f = open("new.txt", "w+")
except FileNotFoundError:
    print("No File Found")

os.remove("new.txt")

try:
    f = open("new.txt", "wb")
except FileNotFoundError:
    print("No File Found")

os.remove("new.txt")

try:
    f = open("new.txt", "wb+")
    f.write("Hi Hello")
except FileNotFoundError:
    print("No File Found")
except TypeError:
    print("String cannot be passed")

