import os

try:
    f = open("new.txt", "a")
except FileNotFoundError:
    print("No File Found")

os.remove("new.txt")

try:
    f = open("new.txt", "a+")
except FileNotFoundError:
    print("No File Found")

os.remove("new.txt")

try:
    f = open("new.txt", "ab")
except FileNotFoundError:
    print("No File Found")

os.remove("new.txt")

try:
    f = open("new.txt", "ab+")
except FileNotFoundError:
    print("No File Found")
finally:
    print("Its over")

