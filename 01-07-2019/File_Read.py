try:
    f = open("new.txt", "r")
except FileNotFoundError:
    print("No File Found")

try:
    f = open("new.txt", "r+")
except FileNotFoundError:
    print("No")

try:
    f = open("new.txt", "rb")
except FileNotFoundError:
    print("No")

try:
    f = open("new.txt", "rb+")
except FileNotFoundError:
    print("No")
