import re

str = " How are you. How is everything"

matches = re.search("How ", str)

print(matches)

print(type(matches))

txt = "The rain in Spain Spain"
x = re.search("^The.*Spain$", txt)

if (x):
  print("match found")
else:
  print("No match")

x = re.search(r"\bS\w+", str)
print(x.group())

str = "The rain in Spain"
x = re.search(r"\bS\w+", str)
print(x.span())

