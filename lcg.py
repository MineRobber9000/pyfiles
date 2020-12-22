import time

class LCG:
	def __init__(self,seed=None,a=22695477,c=1,m=(2**32)):
		if seed is None: seed=time.time()
		self.value = seed
		self.a=a
		self.c=c
		self.m=m
	def __enter__(self): return self
	def __exit__(self,*args,**kwargs): return False
	def __call__(self):
		self.value = (self.a*self.value + self.c)%self.m
		return self.value
