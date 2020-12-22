from contextlib import AbstractContextManager
import io, sys

class CaptureContext(AbstractContextManager):
	def __init__(self):
		self.file = io.StringIO()
	def __enter__(self):
		self.oldso, sys.stdout = sys.stdout, self.file
		return
	def __exit__(self,*args):
		sys.stdout=self.oldso
	def read(self):
		self.file.seek(0)
		return self.file.read()
	def clear(self):
		retach = False
		if sys.stdout==self.file:
			self.__exit__()
			retach = True
		del self.file
		self.file = io.StringIO()
		if retach:
			self.__enter__()
