from datetime import datetime

class Account:
	def __init__ (self,first_name,last_name):
		self.first_name=first_name
		self.last_name=last_name
		self.balance=0
		self.deposits=[]
		self.withdrawal=[]
		self.loan=0
	def welcome(self):
		return "Dear {} {} your current balance is {}".format(self.first_name,self.last_name,self.balance)
	def deposit(self,amount):
		time=datetime.now()
		object={"time":time, "amount":amount}

		self.deposits.append(object)
		self.balance=self.balance + amount
		text="Dear {} {} you have deposited {}".format(self.first_name,self.last_name,amount)
		return text
	def withdraw(self,amount):
		time=datetime.now()
		object={"time":time,"amount":amount}

		self.withdrawal.append(object)
		withdrawal=amount
		if amount>self.balance:

		   return "insufficient funds"
		else :
			self.balance=self.balance - amount
			msg="Dear {} {} you have withdrawn {}".format(self.first_name,self.last_name,amount)
			return msg
	def showbalance(self):
		showbalance = self.balance
		text="Dear {} {} your new balance is {}".format(self.first_name,self.last_name,self.balance)
		return text
	def show_deposit(self):
		for deposit in self.deposits:
			time=deposit["time"]
			formated_time=time.strftime("%c")
			amount=deposit["amount"]
			print("On {} you deposited {}".format(formated_time,amount))
	def show_withdrawal(self):
		for withdraw in self.withdrawal:
			time=withdraw ["time"]
			formated_time=time.strftime("%c")
			amount=deposit[amount]
			print("On {} you deposited {}".format(formated_time,amount))

    def give_loan(self,get_loan):
        loan = get_loan
        total = 0
        for y in self.deposits:
                          
            amount= y["amount"]
            total+=amount
        

         if len(self.deposits)>=5 and c<total/3 and self.loan==0:
            self.loan = self.loan + get_loan
            print("Dear customer your loan of {} has been approved".format(c))



    def repay_loan(self,reward):
        
        payment = reward

        self.loan.extend(reward)

        self.loan = self.loan-reward
        excess_payment = self.deposit.append(deposit)

        msg = "Dear customer you have paid kes {} your remaining loan balance is now {}".format(d,self.loan)
        print(msg)
