class rectangle:

    def __init__(self,width,length):
        self.width = width
        self.length = length

    def area(self):
        return self.width * self.length

    @staticmethod
    def numlist (area):
        list1 = []
        for x in range(1,area):
            for y in range(1,area):
                if x*y == area:
                    xy = (x,y)
                    list1.append(xy)
        return list1

rec1 = rectangle(10,20)
print rec1.area()
print rectangle.numlist(40)
