import re
str = "The rain in Spain"
x = re.sub("\s", "9", str)
print(x)

x = re.sub("\s", "9", str, 2)
print(x)