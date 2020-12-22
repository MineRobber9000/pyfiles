def encode(data,n=1):
	data[n] = data[n-1] ^ data[n]
	if (n+1)<len(data):
		return encode(data,n+1)

def decode(data,n=None):
	n = len(data)-1 if n is None else n
	data[n] = data[n-1] ^ data[n]
	if (n-1)>0:
		decode(data,n-1)

def display(payload):
	print("PAYLOAD:")
	print(" - {} item{}".format(len(payload),"s" if len(payload)!=1 else ""))
	print(" - Numbers: {}".format(", ".join(str(s) for s in payload)))
	print(" - Hex: {}".format(" ".join("{:02X}".format(s) for s in payload)))
	print(" - Text: {}".format("".join(chr(s) if s<128 else "~{:02X}~".format(s) for s in payload)))

if __name__=="__main__":
	print("Encoding test:")
	test = [ord(s) for s in "test"]
	display(test)
	encode(test)
	display(test)
	assert test==[116,17,98,22]
	print("Decoding test:")
	decode(test)
	display(test)
	assert test==[ord(s) for s in "test"]
