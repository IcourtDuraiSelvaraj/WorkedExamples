import re

str = "How are you. How is everything"

matches = re.findall("how", str)
print(matches)

matches = re.findall("How", str)
print(matches)
