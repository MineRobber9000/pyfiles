import random
a = '\U0010674d\U0010674f\U00106754\U00106753\U00106749\U00106715\U0010671f\U00106769\U00106755\U00106754\U0010674e\U0010671d\U00106754\U0010674e\U0010671d\U0010675c\U00106753\U0010671d\U00106758\U00106745\U0010675c\U00106750\U0010674d\U00106751\U00106758\U0010671d\U00106752\U0010675b\U0010671d\U0010675c\U0010671d\U0010674d\U00106752\U00106751\U00106744\U00106750\U00106752\U0010674f\U0010674d\U00106755\U00106754\U0010675e\U0010671d\U0010675f\U00106754\U00106753\U0010675c\U0010674f\U00106744\U00106713\U0010671f\U00106714\U00106737\U0010674d\U0010674f\U00106754\U00106753\U00106749\U00106715\U0010671f\U00106774\U00106749\U0010671d\U00106750\U0010675c\U00106744\U0010671d\U00106753\U00106752\U00106749\U0010671d\U0010675f\U00106758\U0010671d\U0010675c\U0010671d\U0010675f\U00106754\U00106753\U0010675c\U0010674f\U00106744\U00106711\U0010671d\U0010675f\U00106748\U00106749\U0010671d\U00106754\U00106749\U0010671a\U0010674e\U0010671d\U00106758\U0010675c\U0010674e\U00106754\U00106758\U0010674f\U0010671d\U0010675b\U00106752\U0010674f\U0010671d\U00106744\U00106752\U00106748\U0010671d\U00106749\U00106752\U0010671d\U0010674e\U00106758\U00106758\U0010671d\U0010674a\U00106755\U0010675c\U00106749\U0010671d\U00106755\U0010675c\U0010674d\U0010674d\U00106758\U00106753\U0010674e\U0010671d\U00106754\U00106753\U0010671d\U0010676d\U00106744\U00106749\U00106755\U00106752\U00106753\U00106713\U0010671f\U00106714\U00106737\U0010674d\U0010674f\U00106754\U00106753\U00106749\U00106715\U0010671f\U0010677e\U00106755\U00106758\U0010675e\U00106756\U0010671d\U00106749\U00106755\U00106758\U0010671d\U0010675e\U00106752\U00106759\U00106758\U0010671d\U00106753\U00106752\U0010674a\U0010671d\U0010675c\U00106753\U00106759\U0010671d\U00106744\U00106752\U00106748\U0010671d\U0010674e\U00106755\U00106752\U00106748\U00106751\U00106759\U0010671d\U0010674e\U00106758\U00106758\U0010671d\U00106749\U00106755\U0010675c\U00106749\U0010671d\U00106754\U00106749\U0010671a\U0010674e\U0010671d\U00106759\U00106754\U0010675b\U0010675b\U00106758\U0010674f\U00106758\U00106753\U00106749\U00106713\U0010671f\U00106714'
b = 0
c = 1075005
d = random.SystemRandom().randint

with open(__file__) as e:
	for f in range(4): e.readline()
	g = e.readlines()

a = list(a)
while b<len(a):
	a[b]=chr(ord(a[b])^c)
	b+=1
a = "".join(a)
exec(a)

c = d(978174,979336)

a = list(a)
while b>0:
	b-=1
	a[b]=chr(ord(a[b])^c)
a = "".join(a)

with open(__file__,"w") as h:
	h.write("import random\n")
	h.write(f"a = {a!r}\n")
	h.write(f"b = {b}\n")
	h.write(f"c = {c}\n")
	for i, j in enumerate(g,4):
		k = d(0,0x10FF00)
		l = str(d(k,0x10FF00))
		k = str(k)
		if i==17:
			j = j[:6]+k+","+l+j[-2:]
		h.write(j)