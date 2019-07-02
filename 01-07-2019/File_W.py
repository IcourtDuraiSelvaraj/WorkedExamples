from pathlib import _Accessor


def fileAvailabilty():
    try:
        file = open("fileWrite.txt", "x")
    except FileExistsError:
        print("File Already Exixts")



def loadData():
    try:
        fileptr = open("fileWrite.txt", "w")

        fileptr.write("\nPython is the modern day language. It makes things so simple.")

    except FileNotFoundError:
        print("File Not Found")
    except TypeError:
        print("Methods should be proper")

def dataAppend():
    try:
        fileptr = open("file.txt", "a");

        fileptr.write("\nPython is the modern day language. It makes things so simple.")

        fileptr = open("file.txt", "r");

        for i in fileptr:
            print(i)
    except FileNotFoundError:
        print("File Found")

def dataDisplay():
    try:
        fileptr = open("fileWrite.txt", "r");

        for i in fileptr:
            print(i)
    except FileNotFoundError:
        print("File Not Found")

def methods():
    try:
        file = open("file.txt", "r")
        print(file.seek(4))
        print(file.tell())

    except TypeError:
        print()


if __name__ == '__main__':
    fileAvailabilty()
    methods()
    loadData()
    dataDisplay()
    dataAppend()
