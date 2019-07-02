dict_data = {}
print(dict_data)
dict_data ={
    'name': 'durai',
    'age' : 21,
    'mobile' : 8383838383
}
dict_data.clear()
print(dict_data)

dict_data = {
    'name': 'durai',
    'age': 21,
    'mobile': 8383838383,
    'address':{
        'no' : 21,
        'street': 'Valparai main road',
    }
}
print(dict_data)

d = dict_data.copy()
print(d)

print(d.fromkeys(dict_data))
print(d)


keys = ['name', 'age', 'address']
values = []

for i in range(3):
    values.append(input("Enter the "))
print(values)
print(dict.fromkeys(keys,values))
print(dict_data.setdefault('name'))
