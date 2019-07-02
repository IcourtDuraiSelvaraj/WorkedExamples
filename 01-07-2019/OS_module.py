import os
print(os.name)

print("Current Working Directory", os.getcwd())

fd = "GFG.txt"

# popen() is similar to open()
file = open(fd, 'w')
file.write("Hello")
"""
os.close(file) -- - Error Occurred
"""
file.close()
file = open(fd, 'r')
text = file.read()
print(text)

# popen() provides a pipe/gateway and accesses the file directly
file1 = os.popen(fd, 'w')
file1.write("Hello")

file1.close()

os.rename('GFG1.txt', 'gfg.txt')