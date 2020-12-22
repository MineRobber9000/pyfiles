def roll(s):
	import re, random
	m = re.match(r"(\d+)d(\d+)(\+\d+|\-\d+)?",s)
	if not m: return
	num, sides, mod = m.groups()
	if mod is None: mod="0"
	num = int(num)
	sides = int(sides)
	mod = int(mod)
	out = dict()
	out["individual_rolls"]=[random.randint(1,sides) for i in range(num)]
	out["total"]=sum(out["individual_rolls"])+mod
	return out
