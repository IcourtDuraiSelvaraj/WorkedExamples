import re

try:
    str = "How are you. How is everything"

    matches = re.search("z", str)

    print(matches.span())

    print(matches.group())

    print(matches.string)

except AttributeError:
    print("Match Not Found")

try:
    str = "How are you. How is everything"

    matches = re.search("How", str)

    print(matches.span())

    print(matches.group())

    print(matches.string)

except AttributeError:
    print("Match Not Found")