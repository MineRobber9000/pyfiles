from hooks import hooked

@hooked
def square(x):
	"""Squares x."""
	return x**2

@square.hook()
def float_from_it(func,args,kwargs,ret):
	return float(ret)

def func_of_arg_is_ret(func,args,kwargs,ret):
	return "{} of {} is {}".format(func.__name__,args[0],ret)

def halve_arg(func,args,kwargs):
	if func.__name__=="square":
		args = list(args)
		args[0] = args[0]/2
		return tuple(args), kwargs
	return args, kwargs

print("{} - {}".format(square.__name__,square.__doc__))
print(square(5)) # 25.0
square.clear_hooks()
square.add_hook(func_of_arg_is_ret)
print(square(5)) # square of 5 is 25
square.add_hook(halve_arg,True)
print(square(5)) # square of 2.5 is 6.25
