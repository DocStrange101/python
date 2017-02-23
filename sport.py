class sportsteam:
    numplayers = 201
    wins = 8
    losses = 7
    def __init__(self, first,last,position,jersey):
        self.first = first
        self.last = last
        self.position = position
        self.jersey = jersey

    def fullname(self):
        return self.first + ' '+ self.last

    def salary(self, basesalary,gamesplayed):
        ret


p1 = sportsteam('Dave','Speederton','RB',5)
p1.basesalary
print p1.fullname()
