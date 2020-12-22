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
