from functools import wraps

class IncorrectTypeException(Exception): pass

def runtime_check(f):
	ann = dict()
	ann.update(f.__annotations__)
	if "return" in ann: # we don't care about return values
		del ann["return"]
	@wraps(f)
	def __decorated(*args):
		args_ann = list(ann.values())
		if len(args)!=len(args_ann):
			raise TypeError
		for i in range(len(args)):
			if type(args[i])!=args_ann[i]:
				index = i+1
				raise IncorrectTypeException(f"argument {index}, expected {args_ann[i].__name__}, got {type(args[i]).__name__}")
		return f(*args)
	return __decorated

@runtime_check
def square(x: int):
	return x**2

@runtime_check
def pow(n: int, p: int):
	return n**p
