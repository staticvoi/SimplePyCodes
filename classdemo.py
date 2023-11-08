# eg humans are class
# having some common properties like name gender occupation
# having methods like speak write read
# class is abstraction of some entity having central prop like attributes and methods

# object- specific instance
# eg tom cruise is obj of human class

class Human:
    def __init__(self,n,o): #has common prop, self is class itself
        self.name =n
        self.occupation=o
    
    def do_work(self):
        if self.occupation == 'tennis player':
            print(self.name," plays tennis")
        elif self.occupation == 'actor':
            print(self.name," acts")

    def speaks(self):
        print(self.name," says how are you")


tom = Human("tom","tennis player")
tom.do_work()
tom.speaks


deep = Human("deepika","actor")
deep.do_work()
deep.speaks