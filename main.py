import screen
import random
screen.sx = 64
screen.sy = 64

def tickall():
    global people
    for x in people:
        x.ontick()
    screen.updscn()

def makechild():
    global people
    people += [Person(cindex=len(people))]

class Person():
    dead = False
    age = 0
    energy = 100
    resting = False
    def __init__(self, cindex, HP=random.randrange(90, 120), LifeEx=random.randrange(70, 110), x=random.randrange(1,31), y=random.randrange(1,31)):
        self.HP = HP
        self.LifeEx = LifeEx
        self.x = x
        self.y = y
        self.settarget()
        self.cindex = cindex
        screen.scnmem += [[0,0," "]]
    def ontick(self):
        global people
        if self.LifeEx < 1 or self.HP < 1:
            self.dead = True
            screen.scnmem[self.cindex] = [self.x, self.y, "d"]
        else:
            self.LifeEx -= 1
            self.age += 1
            if self.energy < 40:
                self.resting = True
            if not self.resting:
                self.move()
                if random.randint(0, 32) == 1:
                    makechild()
                screen.scnmem[self.cindex] = [self.x, self.y, "a"]
            else:
                if self.energy < 50:
                    self.energy += 1
                    self.LifeEx -= 1
                    screen.scnmem[self.cindex] = [self.x, self.y, "r"]
                else:
                    self.resting = False
    def settarget(self):
        self.tx = random.randrange(1,63)
        self.ty = random.randrange(1,63)
    def move(self):
        if not (self.x == self.tx and self.y == self.ty):
            self.x += self.getdx()
            self.y += self.getdy()
            self.LifeEx += random.randint(1,2)
            self.energy -= random.randint(1,4)
        else:
            self.settarget()
    def getdx(self):
        if self.tx > self.x:
            out = 1
        elif self.tx == self.x:
            out = 0
        else:
            out = -1
        return out
    def getdy(self):
        if self.ty > self.y:
            out = 1
        elif self.ty == self.y:
            out = 0
        else:
            out = -1
        return out


people = [Person(cindex=i) for i in range(100)]
tickall()
while not screen.getkey() == "esc":
    tickall()