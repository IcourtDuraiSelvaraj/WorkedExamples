""""
Mutable Object... List, Set, Dictionary
Immutable Object ... int, float, char, string, complex, bool, tuple
"""

#----List---#

list1 = [1,2,3,4]
list2 = list1

print("id of list1",id(list1))
print("id of list2",id(list2))

list2.append(2)
print("id of list1",id(list1))
print("id of list2",id(list2))
print(list1)
print(list2)