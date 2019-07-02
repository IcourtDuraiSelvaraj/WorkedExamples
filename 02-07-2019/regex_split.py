import re

str = "How are you. How is everything"
data = re.split('are', str)
print(data)

data = re.split('how', str)
print(data)

data = re.split('is', str)
print(data)