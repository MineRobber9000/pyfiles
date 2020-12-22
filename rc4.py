def gen_keystream(key):
	S = list(range(256))
	j = 0
	for i in range(256):
		j = (j + S[i] + key[i % len(key)]) % 256
		S[i], S[j] = S[j], S[i]
	return S

def crypt(S,M):
	i = 0
	j = 0
	k = 0
	while k < len(M):
		i = (i+1)%256
		j = (j+S[i])%256
		S[i], S[j] = S[j], S[i]
		yield M[k]^S[(S[i]+S[j])%256]
		k += 1
