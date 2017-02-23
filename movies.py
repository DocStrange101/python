class movies(object):

    def __init__ (self,title,genra,runtime):
        self.title = title
        self.genra = genra
        self.runtime = runtime

    def time(self):
        return "the total time of the movie is %s minuties" %self.runtime

    def Totaltime(self,mins):
        return "the total total time is %s mintues" %(self.runtime + mins)

    def allThree(self):
        return "the title is %s the genra is %s and the runtime is %s" %(self.title, self.genra,self.runtime)

rougeOne = movies("Rouge One: A Star Wars story", "sci-fi", 150)

Hobbit = movies("The Hobbit: An Unexpected Journey","fantasy/adventure",180)

civilWar = movies("Captian America: Civil War","action/superhero",140)

Avengers = movies('The Avengers','action/sci-fi',120)

print rougeOne.title

print rougeOne.Totaltime(20)

print civilWar.allThree()
