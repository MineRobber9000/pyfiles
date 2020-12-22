import math

def frange(s,e,st=1):
	v = s
	while v<=e:
		yield v
		v+=st

def uniq(l):
	d = {x: l.index(x) for x in l}
	return list(d.keys())

def factors(n):
	m = math.sqrt(n)
	step1 = []
	for i in frange(1.,m):
		if (n%i)==0:
			step1.append(int(i))
	ret = []
	ret.extend(step1)
	for factor in step1:
		ret.append(n//factor)
	ret.sort()
	return uniq(ret)
