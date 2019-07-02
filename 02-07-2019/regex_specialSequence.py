import re


str = 'The Moon is far from the earth hero 456'
x = re.findall("\AThe", str)
print(x)
x = re.findall("\Ahe", str)
print(x)

x = re.findall(r"\bThe",str)
print(x)

x = re.findall(r"\bthe",str)
print(x)

x = re.findall(r"\bhe",str)
print(x)

x = re.findall(r"the\b",str)
print(x)

x = re.findall(r"\Bthe", str)
print(x)
x = re.findall(r"\Bero", str)
print(x)

x = re.findall(r"Moo\B", str)
print(x)
x = re.findall(r"ero\B", str)
print(x)

x = re.findall("\d", str)
print(x)

str = 'The Moon is far from the earth hero!'
x = re.findall("\D", str)
print(x)
print(x[0])

x = re.findall("\s", str)
print(x)

x = re.findall("\S", str)
print(x)

x = re.findall("\w", str)
print(x)

x = re.findall("\W", str)
print("spl character ",x)

x = re.findall("earth\Z", str)
print("spl character ",x)

x = re.findall("hero!\Z", str)
print("spl character ",x)
