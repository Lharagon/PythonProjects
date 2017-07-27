class Bike(object):
	def __init__(self, price, max_speed):
		self.price = price
		self.max_speed = max_speed
		self.miles = 0
	def displayinfo(self):
		print self.price, self.max_speed, self.miles
	def ride(self):
		print "Riding..."
		self.miles += 10
		return self
	def reverse(self):
		print "Reversing..."
		if self.miles >= 5:
			self.miles -= 5
		else:
			self.miles = 0
		return self

first = Bike(500, 20)
second = Bike(300, 10)
third = Bike(200, 5)

first.ride()
first.ride()
first.ride()
first.reverse()
first.displayinfo()

second.ride()
second.ride()
second.reverse()
second.reverse()
second.displayinfo()

third.reverse()
third.reverse()
third.reverse()
third.displayinfo()