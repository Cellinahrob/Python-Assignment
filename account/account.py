class Account:
	def __init__ (self,first_name,last_name,balance):
		self.first_name=first_name
		self.last_name=last_name
		self.balance=balance
	def welcome(self):
		return "Dear {} {} your current balance is {}".format(self.first_name,self.last_name,self.balance)
	def deposit(self,x):
		deposit=x
		self.balance=self.balance + x
		text="Dear {} {} you have deposited {}".format(self.first_name,self.last_name,x)
		return text
	def withdraw(self,z):
		withdraw=z
		if z>self.balance:

		   return "insufficient funds"
		else :
			self.balance=self.balance - z
			msg="Dear {} {} you have withdrawn {}".format(self.first_name,self.last_name,z)
			return msg
	def showbalance(self):
		showbalance = self.balance
		text="Dear {} {} your new balance is {}".format(self.first_name,self.last_name,self.balance)
		return text
