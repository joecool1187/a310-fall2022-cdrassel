class Creature:
    def __init__(self, name):
        self.name = name
        print("Creature " + self.name + " created.")
    def talk(self):
        return "My name is " + self.name + " and I am a " + type(self).__name__ + self.makeSound();
    def makeSound(self):
        return ""

        
Creature("Joe")
me = Creature("Joe")
me
me.talk()
# Creature("Joe").talk()
# Creature("Kate")
# you = Creature("Kate")

