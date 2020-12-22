import random, string, os, socket, time

_BASE36 = string.digits+string.ascii_lowercase
def _to_base36(n: int) -> str:
	if n<0: raise ValueError("Cannot base36-encode a negative number")
	out=""
	while n!=0:
		n,i = divmod(n,36)
		out=_BASE36[i]+out
	return out

_pad = lambda s,l,c="0": s.rjust(l,c)[-l:]

_rng = random.SystemRandom()

def _random_block():
	return _pad(_to_base36(_rng.randint(0,36**4)),4)

class CUIDGen:
	def __init__(self):
		pid_block = _pad(_to_base36(os.getpid()),2)
		hostname = socket.gethostname()
		hostname_block = _pad(_to_base36(sum(map(ord,hostname))+len(hostname)+36),2)
		self.fingerprint=pid_block+hostname_block
		self._counter=-1
	@property
	def counter(self):
		self._counter+=1
		if self._counter>=(36**4):
			self._counter=0
		return self._counter
	def cuid(self):
		out="c"
		out+=_to_base36(int(time.time()*1000))
		out+=_pad(_to_base36(self.counter),4)
		out+=self.fingerprint
		out+=_random_block()
		out+=_random_block()
		return out

_GENERATOR = CUIDGen()

def cuid(): return _GENERATOR.cuid()
