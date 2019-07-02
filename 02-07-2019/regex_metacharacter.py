import re

str = 'Hi Heello Welcome to my channel 1997'

x = re.findall("[a-m]", str)
print(x)

x = re.findall("\d", str)
print(x)

x = re.findall("He..o", str)
print(x)

x = re.findall("^Hi", str)
print(x)

x = re.findall("^Hello", str)
print(x)

x = re.findall('1997$',str)
print(x)

x = re.findall('channel$',str)
print(x)

x = re.findall('o*', str)
print(x)

x = re.findall('o+', str)
print(x)

x = re.findall('el{2}', str)
print(x)

x = re.findall('el|come', str)
print(x)

