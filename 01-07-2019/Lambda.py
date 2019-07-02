def table(n):
    b1  = lambda a:a*n; # a will contain the iteration variable i and a multiple of n is returned at each function call
    return b1
n = int(input("Enter the number?"))
b = table(n) #the entered number is passed into the function table. b will contain a lambda function which is called again and again with the iteration variable i
for i in range(1,11):
    print(n,"X",i,"=",b(i)); #the lambda function b is careturn lambda a:a*n;lled with the iteration variable i,