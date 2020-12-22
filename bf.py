import sys,enum

class Tape:
	def __init__(self):
		self.tape = dict()
		self.mp=0
	def incp(self):
		self.mp+=1
	def decp(self):
		self.mp-=1
	def inc(self):
		self.set(self.get()+1)
	def dec(self):
		self.set(self.get()-1)
	def get(self):
		return self.tape.get(self.mp,0)
	def set(self,v):
		self.tape[self.mp]=(v&0xFF)
	def reset(self):
		self.__init__()

class BFInterpreter:
	def __init__(self):
		self.tape=Tape()
		self.input_buffer=""
		self.last_char=""
	def _loop_tbl(self,p):
		deck = []
		out = dict()
		for i,c in enumerate(p):
			if c=="[":
				deck.append(i)
			elif c=="]":
				d = deck.pop(-1)
				out[i]=d
				out[d]=i
		if len(deck)>0: raise Exception("Unbalanced loops!")
		return out
	def run(self,prog,input_func=None):
		if input_func is None: input_func = self.read
		self.tape.reset()
		self.input_buffer=""
		self.last_char=""
		looptbl = self._loop_tbl(prog)
		i=0
		while i<len(prog):
			c=prog[i]
			if c=="+": self.tape.inc()
			elif c=="-": self.tape.dec()
			elif c==">": self.tape.incp()
			elif c=="<": self.tape.decp()
			elif c=="[" and self.tape.get()==0: i=looptbl[i]
			elif c=="]" and self.tape.get()!=0: i=looptbl[i]
			elif c==".": self.write(self.tape.get())
			elif c==",": self.tape.set(input_func())
			i+=1
	def write(self,c):
		self.last_char=chr(c)
		sys.stdout.write(chr(c))
		sys.stdout.flush()
	def read(self):
		if self.input_buffer:
			self.input_buffer, c = self.input_buffer[1:], self.input_buffer[0]
			return ord(c)
		try:
			if self.last_char and self.last_char!="\n": self.write("\n")
			self.input_buffer = input("Give input: ")
		except EOFError:
			return 0
		self.input_buffer, c = self.input_buffer[1:], self.input_buffer[0]
		return ord(c)

class MockInput:
	def __init__(self,v):
		self.v=v
		self.i=0
	def _on_eof(self):
		return 0
	def __call__(self):
		if self.i>=len(self.v): return self._on_eof()
		c = ord(self.v[self.i])
		self.i+=1
		return c

class StdinInput(MockInput):
	def __init__(self):
		super(StdinInput,self).__init__(sys.stdin.read())

if __name__=="__main__":
	_, filename = sys.argv
	with open(filename) as f: prog=f.read()
	i = BFInterpreter()
	i.run(prog,StdinInput())
