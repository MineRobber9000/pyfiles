def pad(s,l,c=" "):
	return (s+(c*l))[:l]

class LineBuffer:
	def __init__(self,s,l=None):
		if l is None:
			l = len(s)
		self.s = s
		self.l = l
		self.draw()

	def set(self,s):
		self.s = s
		if len(self.s)>self.l:
			self.l = len(self.s)
		elif len(self.s)<self.l:
			self.s = pad(self.s,self.l)

	def get(self):
		return self.s

	def draw(self):
		print("\r{}".format(self.s),end="")
