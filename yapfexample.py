class GetFixed:
	def __init__(self,value):
		self.value=value
	def __get__(self,k):
		return self.value
