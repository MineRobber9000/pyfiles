import random

class Stock:
	def __init__(self,ticker,name,value=1000.00,risk=15,mutability=50):
		self.ticker = ticker
		self.name = name
		self.value = value
		self.risk = risk
		self.mutability = mutability
	def tick(self,riskroll,modroll,factorroll):
		if riskroll<(self.mutability/100):
			if (riskroll/(self.mutability/100))>.5:
				self.risk+=1
			else:
				self.risk-=1
		if modroll<(self.risk/100):
			self.value*=(factorroll+.5)
	def randomTick(self):
		self.tick(random.random(),random.random(),random.random())
	def __str__(self):
		return "{} ({}); Value: ${:1.2f} ({}% risk)".format(self.name,self.ticker,self.value,self.risk)
	def __repr__(self):
		return "<{} ({}); Value: ${:1.2f} ({}% risk, {}% mutability)>".format(self.name,self.ticker,self.value,self.risk,self.mutability)

class Market:
	def __init__(self,stocks,cond=0.5):
		self.stocks = stocks
		self.cond = cond
	def tick(self):
		if self.cond==0 or random.random()<0.25:
			self.cond+=(random.random()/4)-.25
			if self.cond<0: self.cond=0
			if self.cond>.90: self.cond=.90
		if random.random()<self.cond: # market boom
			for stock in self.stocks:
				stock.tick(1,0,2)
		for stock in self.stocks:
			stock.randomTick()
	def __str__(self):
		return "\n".join([str(x) for x in self.stocks])
	def __repr__(self):
		return repr(self.stocks)
