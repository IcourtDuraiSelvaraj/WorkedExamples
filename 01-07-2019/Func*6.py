def printme(*names):
    print("type of passed argument is ",type(names))
    print("printing the passed arguments...")
    for name in names:
        print(name)

i = 1

while i!=0:
    print(i)
    a = input()
    if a != 0:
        printme(a)
    else:
        i = 0
        break


