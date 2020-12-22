G = dict()
for x in range(256):
	for y in range(256):
		if x==y:
			G[x,y]=""
			continue
		delta=y-x
		if delta>128: delta-=256
		if delta<-128: delta+=256
		if delta>=0:
			G[x,y]="+"*delta
		else:
			G[x,y]="-"*abs(delta)
imp=True
while imp:
	imp=False
	for x in range(256):
		for n in range(40):
			for d in range(40):
				if n==d: continue
				j=x
				y=0
				for i in range(256):
					if j==0: break
					j=(j-d+256)&0xFF
					y=(y+n)&0xFF
				if j==0:
					s="["+("-"*d)+">"+("+"*n)+"<]>"
					if len(s)<len(G[x,y]):
						G[x,y]=s
						imp=True
				j=x
				y=0
				for i in range(256):
					if j==0: break
					j=(j+d)&0xFF
					y=(y-n+256)&0xFF
				if j==0:
					s="["+("+"*d)+">"+("-"*n)+"<]>"
					if len(s)<len(G[x,y]):
						G[x,y]=s
						imp=True
for x in range(256):
	for y in range(256):
		for z in range(256):
			if len(G[x,z]+G[z,y])<len(G[x,y]):
				G[x,y]=G[x,z]+G[z,y]

def to_bf(s):
	s = s.encode("ascii")
	p = ""
	l = 0
	for i in range(len(s)):
		p+=G[l,s[i]]+"."
		l=s[i]
	return p
