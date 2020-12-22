values=dict(I=1,V=5,X=10,L=50,C=100,D=500,M=1000)

def split_lower(s):
	if len(s)==1: return [s]
	i=len(s)-1
	o=[]
	while i>0:
		oi = i*1
		while i>0 and values[s[i-1]]<values[s[i]]:
			i-=1
		o.append(s[i:oi+1])
		i-=1
	if values[s[0]]>=values[s[1]]: o.append(s[0])
	return o[::-1]

def handle(p):
	if len(p)==1: return values[p]
	elif len(p)==2: return values[p[1]]-values[p[0]]
	else: raise SyntaxError("Invalid numeral segment "+p)

def atoi(s):
	parts = list(map(handle,split_lower(s)))
	return sum(parts)

PARTS = dict()
PARTS[1]="I X C M".split()
PARTS[2]="II XX CC MM".split()
PARTS[3]="III XXX CCC MMM".split()
PARTS[4]="IV XL CD MMMM".split()
PARTS[5]="V L D MMMMM".split()
PARTS[6]="VI LX DC MMMMMM".split()
PARTS[7]="VII LXX DCC MMMMMMM".split()
PARTS[8]="VIII LXXX DCCC MMMMMMMM".split()
PARTS[9]="IX XC CM MMMMMMMMM".split()

def itoa(n):
	if n>9999:
		raise SyntaxError("Why are you doing this to yourself?")
	p = []
	for i,c in enumerate(str(n)[::-1]):
		if int(c): p.append(PARTS[int(c)][i])
	return ''.join(p[::-1])
