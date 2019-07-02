data  = [1, 2, 3]
data1 = [1, 2, 3]
data2 = {1, 2, 3}
data3 = list(data2)


print("data id....", id(data))
print("data1 id...", id(data1))
print("data2 ...id ", id(data2))
print("data3 id...", id(data3))


print("data is data1..")
if data is data1:
    print("true")
else:
    print("false")

print("Using == operator..")

if data1 == data2:
    print("true")
else:
    print("false")

print("Using is....")

if data1 is data2:
    print("true")
else:
    print("false")

print("-----------------")


if data1 == data3:
    print("true")
else:
    print("false")



if data1 is data3:
    print("true")
else:
    print("false")

d_data = tuple(data)
print(d_data)

print(id(data))
print(id(data[0]))
print(id(data[1]))
