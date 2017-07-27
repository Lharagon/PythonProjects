class Animal(object):

	def __init__(self, name):
		self.name = name
		self.health = 100

	def walk(self):
		self.health -= 1

	def run(self):
		self.health -= 5

	def displayHealth(self):
		print "Name: %s" % (self.name)
		print "Health: %s" % (self.health)

beast = Animal("Beast")

beast.walk()
beast.walk()
beast.walk()
beast.run()
beast.run()
beast.displayHealth()

class Dog(Animal):
    
    def __init__(self, name):
        Animal.__init__(self, name)
        self.health = 150

    def pet(self):
        self.health += 5

fluffy = Dog("fluffy")

fluffy.walk()
fluffy.walk()
fluffy.walk()
fluffy.run()
fluffy.run()
fluffy.pet()
fluffy.displayHealth()

class Dragon(Animal):
    
    def __init__(self, name):
        Animal.__init__(self,name)
        self.health = 170
    def fly(self):
        self.health -= 10
    def displayHealth(self):
        print "This is a Dragon!"
        Animal.displayHealth(self)
    

scally = Dragon("Scally")

scally.walk()
scally.walk()
scally.walk()
scally.run()
scally.run()
scally.fly()
scally.fly()
scally.displayHealth()