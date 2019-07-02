class SetDataType:

    def setdifference(self):

        #difference in set and dictionary
        set_data = {}
        print("Empty set...",type(set_data))

        set_data = {1}
        print(set_data)
        print(type(set_data))

    def runtimeinput(self):
        #add data during runtime
        set_data1 =set()
        m = int(input("Enter no of data"))

        for i in range(m):
            set_data1.add(input("Enter data ",i))
        print(set_data1)

    def set_duplicate_removal(self):
        set_data2 = {1, 'durai', 'raj', 21, 1, 'raj'}
        print("removes duplicate.... ",set_data2)

        #list to tuple
        list_data = [1,2,2,3,4,5,5]
        ss = set(list_data)
        print("list to set to remove duplicate", ss)
        return set_data2

    def setmethods(self, set_data2):
        #add
        set_data2.add('hi')
        print(set_data2)

        #runtime input
        s = input("enter data to add...")
        set_data2.add(s)
        print("data added into set...", set_data2)

        #union method
        set_data3 = {'durai', 'raj', 'selvam','hi'}
        print("Union.....(union method)..... ",set_data2.union(set_data3))
        print("Union....(|)...",set_data2|set_data3)

        print(set_data2)
        print(set_data3)

        #intersection
        print("Common data... ",set_data2.intersection(set_data3))

        #difference
        print("Not a common data ...", set_data2.difference(set_data3))
        print("Not a common data using (-)....", set_data2 - set_data3)

        print("Not a common data ...", set_data3.difference(set_data2))
        print("Not a common data using (-)....", set_data3 - set_data2)

        #clear
        print("clear data in set...", set_data2.clear())


if __name__ == '__main__':
    sd = SetDataType()
    sd.setdifference()
    data = sd.set_duplicate_removal()
    sd.setmethods(data)
    sd.runtimeinput()
