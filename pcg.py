import random, os, math
from hashlib import sha512

SIXTY_FOUR_BITS = (2**64)
THIRTY_TWO_BITS_AND = (2**32)-1
RECIP_THIRTY_TWO_BITS = (2**-32)

def rotate32(n,d):
	return ((n>>d)|(n<<(32-d)))&THIRTY_TWO_BITS_AND

class KhuxkmPCG(random.Random):
	def __init_(self):
		super(KhuxkmPCG,self).__init__()
		self.state=1
	def _rand_statetransition(self):
		self.state=(6364136223846793005*self.state + 23)%SIXTY_FOUR_BITS
	def _rand_output(self):
		return rotate32((self.state^(self.state>>18))>>27,self.state>>59)
	def getstate(self):
		return self.state
	def setstate(self,state):
		self.state=state
	def seed(self,a=None,version=None):
		if a is None: a=int.from_bytes(os.urandom(8),'big')
		if type(a)==float:
			while (a%1)>0: a*=10
			a=int(a)
		elif type(a) in (str, bytes, bytearray):
			if type(a)==str:
				a=a.encode()
			a=int.from_bytes(sha512(a).digest(),'big')
		elif type(a)!=int:
			raise TypeError("Seed must be str, bytes, bytearray, float or int!")
		self.state=a%SIXTY_FOUR_BITS
	def random(self):
		self._rand_statetransition()
		return self._rand_output()*RECIP_THIRTY_TWO_BITS
	def getrandbits(self,k):
		numoutputs = math.ceil(k/32)
		out = ""
		for i in range(numoutputs):
			self._rand_statetransition()
			out+="{:032b}".format(self._rand_output())
		return int(out[:k],2)
