import sys

major = sys.version_info.major

def six(two,three):
	return lambda: two if major==2 else three

def newmodule():
	if major==2:
		return __import__("new").classobj
	elif major==3:
		return lambda name,base,ns: __import__("types").new_class(name,base,dict(),lambda d: d.update(ns))

def wh(cond,func):
	while cond():
		func()

class BrainfuckManual:
	def __init__(self):
		self.mem = {}
		self.dp = 0
		self.globals = globals()
	def add(self):
		return eval("mem.__setitem__(dp,(mem.get(dp,0)+1))",self.globals,self.__dict__)
	def sub(self):
		return eval("mem.__setitem__(dp,(mem.get(dp,0)-1))",self.globals,self.__dict__)
	def left(self):
		return eval("locals().__setitem__('dp',dp-1)",self.globals,self.__dict__)
	def right(self):
		return eval("locals().__setitem__('dp',dp+1)",self.globals,self.__dict__)
	def out(self):
		return eval(six("print chr(mem[dp]),","print(chr(mem[dp]),end='')")(),self.globals,self.__dict__)
	def run(self,p):
		self.i = 0
		self.p = p
		wh(lambda: self.i<len(p),self.tick)
	def tick(self):
		self.c = self.p[self.i]
		{"+":self.add,"-":self.sub,">":self.right,"<":self.left,".":self.out}[self.c]()
		self.i = self.i+1

Brainfuck = (lambda new,globals: new("Brainfuck",(),dict(__init__=lambda self: self.__dict__.update(dict(mem={},dp=0,globals=globals)),add=lambda self: eval("mem.__setitem__(dp,(mem.get(dp,0)+1))",self.globals,self.__dict__),sub=lambda self: eval("mem.__setitem__(dp,(mem.get(dp,0)-1))",self.globals,self.__dict__),left=lambda self: eval("locals().__setitem__('dp',dp-1)",self.globals,self.__dict__),right=lambda self: eval("locals().__setitem__('dp',dp+1)",self.globals,self.__dict__),out=lambda self: eval(six("print chr(mem[dp]),","print(chr(mem[dp]),end='')")(),self.globals,self.__dict__),run=lambda self,p: (self.__dict__.update(dict(i=0,p=p)),wh(lambda: self.i<len(p),self.tick))[0],tick=lambda self: ({"+":self.add,"-":self.sub,"<":self.left,">":self.right}[self.p[self.i]](),eval("locals().__setitem__('i',i+1)",self.globals,self.__dict__))[0])))(newmodule(),globals())
