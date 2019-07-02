
fileptr = open("file.txt", "a");

fileptr.write("\nPython is the modern day language. It makes things so simple.")


fileptr = open("file.txt", "r");


for i in fileptr:
    print(i)