import random

def shuffle(s: str) -> str:
	cs = list(s)
	random.shuffle(cs)
	return "".join(cs)

def divisible(n: int, d: int) -> bool:
	return (n%d)==0

def check_n(s):
	if type(s)==int: s=hex(s)[2:].rjust(16,"0")
	def works(s):
		assert divisible(int(s,16),len(s)),"abcdefghijklmnop"[:len(s)]+" must be divisible by "+str(len(s))
	try:
		assert len(list(set(s)))==16,"Not all unique!"
		assert s[9]=="0","abcdefghij must be divisible by 10"
		works(s[0])
		works(s[0:1])
		works(s[0:2])
		works(s[0:3])
		works(s[0:4])
		works(s[0:5])
		works(s[0:6])
		works(s[0:7])
		works(s[0:8])
		works(s[0:9])
		works(s[0:11])
		works(s[0:12])
		works(s[0:13])
		works(s[0:14])
		works(s[0:15])
		works(s[0:16])
	except AssertionError as e:
		print(e.args[0])
		return False
	return True

rescache = dict()
chs = "0123456789abcdef"

print("trying",chs)
res = check_n(chs)
while not res:
	rescache[chs]=res
	while chs in rescache or chs[9]!="0" or chs[3:6]!="654" or chs[1] not in "02468ace" or chs[7] not in "02468ace" or chs[0] not in "13579bdf": chs=shuffle(chs)
	print("trying",chs)
	res = check_n(chs)
