import stack

market = [
	["MLSE","Miles Entertainment, Inc.",25.00,75],
	["TTWO","Take-Two Interactive, Inc.",110.29,25]
]

global inventory, balance
market = stack.Market([stack.Stock(*stock) for stock in market],1)
inventory = [0 for x in market.stocks]
balance = 1000

def breakDown(inventory,balance):
	global market
	b = sum([market.stocks[i].value*inventory[i] for i in range(len(market.stocks))])+balance
	return "Balance: ${:0.2f} (${:0.2f} cold cash)\nMarket: (condition: {:.0%})\n{!s}".format(b,balance,market.cond,market)

global running
running = True

while running:
	print(breakDown(inventory,balance))
	choice = input("Would you like to [b]uy, [s]ell, or [w]ait?: ").strip()
	if not choice: choice = "w"
	choice = choice.lower()[0]
	if choice == "b":
		s = int(input("Which stock? (top down): "))-1
		a = int(input("How many?: "))
		if balance >= (market.stocks[s].value*a):
			print("Bought {} stock in {}".format(a,market.stocks[s].name))
			inventory[s]+=a
			balance-=(market.stocks[s].value*a)
		else:
			print("You can't afford that many!")
	elif choice == "s":
		s = int(input("Which stock? (top down): "))-1
		a = int(input("How many?: "))
		if inventory[s]>=a:
			print("Sold {} stock in {}".format(a,market.stocks[s].name))
			inventory[s]-=a
			balance+=(market.stocks[s].value*a)
		else:
			print("You don't have that many!")
	elif choice == "w":
		market.tick()
	elif choice == "q":
		running = False
