
class Customer(object):

    def __init__(self,first,last,amt,password):

        self.first = first
        self.last = last
        self.amt = amt
        self.password = password

    def printName(self):
        return self.first + ' ' + self.last

    def printBalance(self,deposit,withdraw):
        return self.amt + deposit - withdraw

    def passChange(self,newPass):
        self.password.replace(newPass)

        class Investor(Customer):
            def __init__(self,first,last,amt,password,stock):
                super(Investor,self).__init__(first,last,amt,password)
                self.stock = {}

                def addStock(self,company,nStock):
                    self.stock.append(company : nStock)



c1 = Customer('Bob','Jones',70,'HELICARRIER12')
i1 = investor ()

print c1.first
