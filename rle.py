def encode(data):
	count = 1
	prev_val = None
	if not data: return []
	for val in data:
		if val!=prev_val:
			if prev_val is not None:
				yield (count, prev_val)
			count = 1
			prev_val=val
		else:
			count+=1
	else:
		yield (count, prev_val)

def decode(encoded):
	data = []
	for count, val in encoded:
		data.extend([val]*count)
	return data
