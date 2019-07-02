List = {1,2,3,4,10,123,22}
Oddlist = list(filter(lambda x:(x*3),List))
print(Oddlist)

# the list contains all the items of the list for which the lambda function evaluates to true
