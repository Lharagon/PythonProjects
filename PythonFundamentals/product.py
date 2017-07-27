
class Product(object):

	def __init__(self, price, item_name, weight, brand, cost):
		self.price = price
		self.item_name = item_name
		self.weight = weight
		self.brand = brand
		self.cost = cost
		self.status = "for sale"

	def sell(self):
		self.status = "Sold"
		return self

	def add_tax(self, tax):
		self.tax = tax
		return self.price + (self.price * self.tax)

	def Return(self, reason, box):
		self.reason = reason
		self.status = "for sale"
		if box == False:
			self.price = self.price - (self.price * 0.20)
		if reason == "defective":
			self.status = reason
			price = 0
		return self

	def Display(self):
		print "Price: $%s" % (self.price)
		print "Item Name: %s" % (self.item_name)
		print "Weight: %slbs" % (self.weight)
		print "Brand: %s" % (self.brand)
		print "Cost: $%s" % (self.cost)
		print "Status: %s" % (self.status)

banana = Product(3, 'banana', 25, 'ban', 1)

banana.Display()
banana.sell()
banana.Display()
banana.add_tax(2)
banana.Display()
banana.Return("defective", False).Display()

