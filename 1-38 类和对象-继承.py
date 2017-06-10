import random as r

class Fish:
    def __init__(self):
        self.x = r.randint(0,10)
        self.y = r.randint(0,10)

    def move(self):
        self.x -= 1
        print('my position is:',self.x, self.y)

class Goldfish(Fish):
    pass

class Carp(Fish):
    pass

class Salmon(Fish):
    pass

class Shark(Fish):
    def __init__(self):
        Fish.__init__(self) #uncover the mean writed before
                            #it can use this way also----super().__init__()
        self.hungry = True

    def eat(self):
        if self.hungry:
            print('the happieness is we don\'t need to worry about the food everyday')
            self.hungry = False
        else:
            print('i am full, i can\'t eat anymore')
            
