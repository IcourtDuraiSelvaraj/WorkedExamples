try:
    f = open("new22.txt", "x")
except FileExistsError:
    print("Already Exists")
