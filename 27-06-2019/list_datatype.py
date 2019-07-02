class ListDataType:
    def nested_list(self):
        list1 = []

        n = int(input("Enter no of data"))
        ##############Nested List##############################
        for i in range(n):
            list1.append([])
            m = int(input("Enter no of records"))
            for j in range(m):
                list1[i].append(input())
                print(id(list1))
        print(list1)

        #######################################################

        #Nested list into single list
        list2 = []
        for datas in list1:
            for data in datas:
                list2.append(data)

        print(list2)

        list3 = []
        for d in list2:
            list3.append(type(d))
        print(list3)
        return list2
        ##Here everything will be taken as string##

    def list_method(self, list2):
        #insert(index, value)
        list4 = ['durai','raj']
        list4.insert(1,'hi')
        print(list4)

        #extend

        list4.extend(list2)
        list2.extend(list4)

        print(list4)
        print(list2)

        #sum()
        li = [1,3,5,1,3,4,5,67,7]
        print("sum...",sum(li))

        #count()
        print("count",li.count(1))

        print(min(li))
        print(max(li))
        print(li.index(1,0,2))

        del li[0]
        print("delete....",li)

        print("pop....",li.pop())
        print("list data....",li)

        #sorting
        print("sorting....",sorted(li))
        print("descending order",li.sort(reverse=True))
        print("ascending order",li.sort(reverse=False))

    def addListObject(self):
        List = ['Mathematics', 'chemistry', 1997, 2000]
        List1 = ['Mathematics', 'chemistry', 1997, 2000]
        List2 = [List1, List]
        print(List2)
        print(List2 * 3)


if __name__ == '__main__':
    lii = ListDataType()
    dat1 = [1, 2, 3]
    dat1 = lii.nested_list()
    lii.list_method(dat1)
    lii.addListObject()