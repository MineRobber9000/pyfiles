import enum, random

class Result(enum.Enum):
	TOO_LOW=0
	CORRECT=1
	TOO_HIGH=2

class GuessStrategy:
	def __init__(self,min,max):
		self.min=min
		self.max=max
		print(f"I'm thinking of a number between {min} and {max}.")
	def guess(self):
		ret = input("Guess a number> ")
		while not ret.isdigit():
			print("Not a number!")
			ret = input("Guess a number> ")
		return int(ret)
	def react(self,guess,result):
		if result==Result.TOO_LOW:
			print(f"{guess} was too low.")
		elif result==Result.TOO_HIGH:
			print(f"{guess} was too high.")
		else:
			print(f"Correct! It was {guess}!")

def guessing_game(min,max,strat=GuessStrategy):
	strat = strat(min,max)
	num = random.randint(min,max)
	found = False
	guesses = 0
	while not found:
		guess = strat.guess()
		guesses+=1
		result = Result.CORRECT
		if guess<num:
			result = Result.TOO_LOW
		elif guess>num:
			result = Result.TOO_HIGH
		strat.react(guess,result)
		found = (result==Result.CORRECT)
	return (num, guesses)

if __name__=="__main__":
	guessing_game(1,100)
