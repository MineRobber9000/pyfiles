from guessing_game import *
import statistics

class Strat(GuessStrategy):
	def __init__(self,min,max):
		self.min=min
		self.max=max
	def guess(self):
		return (self.min+self.max)//2
	def react(self,guess,result):
		if result==Result.TOO_LOW:
			self.min=guess
			print(f"{guess} was too low.")
		elif result==Result.TOO_HIGH:
			self.max=guess
			print(f"{guess} was too high.")
		else:
			print(f"The number was {guess}!")

average = lambda x: round(sum(x)/len(x),2)

if __name__=="__main__":
	length = []
	for i in range(1000):
		number, tries = guessing_game(1,100,Strat)
		length.append(tries)
	print("Average length of attempt:",average(length))
	print("Standard Deviation:",round(statistics.pstdev(length),5))
