# classes is tamlates for objects
# humman is class and rahul is object and properties
# constructore is speial method of class


class Fish:
    def swim(self):
        print("Fish can swim")

    def eat(self):
        print("Fish can eat")


fish = Fish()
fish.swim()
fish.eat()

# override the constructor


class Game:
    def __init__(self,name):
        self.name =name

    def start(self):
        print(self.name,"game is started")

    def end(self):
        print(self.name, "game is stooped")


game = Game("Counter Strike")
game.start()
game.end()
