tokenize = lambda s: s.split()

add = lambda first, second: first+second
sub = lambda first, second: first-second
mul = lambda first, second: first*second
div = lambda first, second: first//second
from math import pow
mod = lambda first, second: first%second

ops = {"+":add,"-":sub,"*":mul,"/":div,"^":pow,"%":mod}

def calculate(s):
	s=tokenize(s)
	l=[]
	for token in s:
		if token.isdigit():
			l.append(int(token))
			continue
		if token in ops:
			second = l.pop()
			first = l.pop()
			l.append(ops[token](first,second))
	return l[-1]
