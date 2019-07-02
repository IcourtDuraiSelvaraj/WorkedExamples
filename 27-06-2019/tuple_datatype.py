class tupleDataType:

    def addRunTime(self):
        # add data in run time

        tup1 = ()
        n = int(input("No of data"))
        for i in range(n):
            tup1 += (input('Enter data'),)

        print(tup1)

    def tupleInitialization(self):
        tupll = (1, 'durai')
        print(tupll)

        #string
        tupll = 'durai'
        print(type(tupll))

        #tuple
        tupll = 1, 'durai', 'Imapct Training'
        print(tupll)
        print(type(tupll))
        return tupll

    def tupleOperation(self, tuple1):
        #count
        print(tuple1)
        print("count....... ",tuple1.count(1))

        #index
        print("Index... ",tuple1.index('durai'))

        #add tuple

        tuple2 = 2, 'raj', 'qwerty', 2
        tup = tuple1 + tuple2
        print(tup)

    def list_to_tuple(self, tupledata):
        #to add data into tuple using list
        datalist = list(tupledata)
        datalist.append('durai97')
        print(type(datalist))
        print(tupledata)
        tupledataa = tuple(datalist)
        print("added data..... ",tupledataa)

        print("print data in seperate...(using slicing operator) ",tupledataa[:2], tupledataa[2:])
        print("print data in single...(using slicing operator) ", tupledataa[:2] + tupledataa[2:])


if __name__ == '__main__':
    td = tupleDataType()
    td.addRunTime()
    tupl = td.tupleInitialization()
    td.tupleOperation(tupl)
    td.list_to_tuple(tupl)