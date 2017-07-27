class Car(object):
	def __init__(self,price,speed,fuel,mileage):
		self.price = price
		self.speed = speed
		self.fuel = fuel
		self.mileage = mileage

		if self.price > 10000:
			self.tax = 0.15
		else:
			self.tax = 0.12

		self.display_all()



	def display_all(self):
		print "Price: " + str(self.price)
		print "Speed: " + str(self.speed)
		print "Fuel: " + str(self.fuel)
		print "Mileage: " + str(self.mileage)
		print "Tax: " + str (self.tax) + "\n"
 

toyota = Car(12000, 50, "Semi Full", 50)
honda = Car(1500, 30, "Full", 10)
chevy = Car(100, 10, "Empty", 10)
BMW = Car(1000000, 5, "No Gas Tank", 3)
Ford = Car(20000, 34, "Full", 79)
mercedes = Car(79, 56, "Half", 89)