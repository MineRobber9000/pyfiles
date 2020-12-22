import re,random
ALPHABET = re.compile("^[A-Za-z]*$")
words = []
with open("/usr/share/dict/words") as f:
	for l in f:
		l = l.strip()
		if not l: continue
		if not ALPHABET.match(l): continue
		words.append(l)

lower = lambda x: x.lower()

def pick4():
	return "".join(map(lower,random.choices(words,k=4)))

def capitalize(s,i):
	if i>=len(s): return s
	if i<(-1*len(s)): return s
	return s[:i]+s[i].upper()+(s[i+1:] if i!=-1 else "")

def fibonacci(s):
	if random.choice("forwards backwards".split())=="forwards":
		a=1
		b=1
		s = capitalize(s,0)
		s = capitalize(s,1)
		i=1
		while i<len(s):
			c=a+b
			a=b
			b=c
			i+=b
			s=capitalize(s,i)
	else:
		a=1
		b=1
		s = capitalize(s,-1)
		s = capitalize(s,-2)
		i=-2
		while i>(-1*len(s)):
			c=a+b
			a=b
			b=c
			i-=b
			if i<len(s): s=capitalize(s,i)
	return s

def password_gen():
	return fibonacci(pick4())

if __name__=="__main__": print(password_gen())
