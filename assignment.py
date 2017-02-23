class MyNumbers(object):

    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c

    def addMethod(self):
        return self.a + self.b + self.c

    def multiply(self):
        return self.a * self.b * self.c

    def middleNum(self):
        a = self.a
        b = self.b
        c = self.c
        if a < b and b > c:
            return b
        if b < a and a > c:
            return a
        if a < c and c > b:
            return c
        else:
            return 'False'

    def Largest(self):


numset1 = MyNumbers(1,2,3)
print numset1.middleNum()
