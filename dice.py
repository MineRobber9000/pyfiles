import random
import re
import six

def get(bs,i):
	if six.PY2:
		return ord(bs[i])
	else:
		return bs[i]

def hashCode(s):
	bs = s.encode("utf-8")
	hash = 0
	for i in range(len(bs)):
		hash = (31*hash+get(bs,i))&0xFFFFFFFF
	return ((hash+0x80000000)&0xFFFFFFFF)-0x80000000

DICE_REGEX = re.compile(r"(\d+)d(\d+)(-\d+|\+\d+)?")

def roll(dice_spec,seed=None):
	if seed is not None:
		if type(seed)==str: seed=hashCode(seed)
		random.seed(seed)
	m=DICE_REGEX.match(dice_spec)
	if m is None: raise Exception("Dice spec invalid!")
	num,sides,mod=m.groups()
	num,sides = int(num), int(sides)
	mod = int(mod) if mod is not None else 0
	roll = dict()
	roll["individual_rolls"]=[random.randint(1,sides) for i in range(num)]
	roll["sum"]=sum(roll["individual_rolls"])+mod
	roll["_modifier"]=mod
	return roll
