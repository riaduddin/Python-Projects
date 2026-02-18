

class Payment:
	def pay(self):
		raise NotImplementedError("Subclass should implement pay method")


class CreditCard(Payment):
	def pay(self):
		return "Credit card payment"

class Paypal(Payment):
	def pay(self):
		return "Credit card payment"

class Crypto(Payment):
	def pay(self):
		return "Credit card payment"


class 

